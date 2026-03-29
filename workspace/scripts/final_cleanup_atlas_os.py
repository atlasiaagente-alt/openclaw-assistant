import json, os, sys, urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN = os.environ['NOTION_TOKEN']
VERSION = '2025-09-03'
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': VERSION,
    'Content-Type': 'application/json',
}


def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}


def safe(label, fn):
    try:
        fn()
        print('ok', label)
    except urllib.error.HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8')
        except Exception:
            pass
        print('error', label, e.code, body[:200])
    except Exception as e:
        print('error', label, repr(e))


def archive(block_id):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{block_id}', {'archived': True})


# Archive leftover blocks that don't belong in the clean structure:
# 1. Old "Atlas | Operacion / Sistema" heading_3 (before the child_pages)
safe('old sys heading', lambda: archive('32d0a0b1-97cc-815f-b40c-cf5b3509ec5d'))
# 2. Old sys description paragraph
safe('old sys desc', lambda: archive('32d0a0b1-97cc-81e0-b501-fabfb357994f'))
# 3. Old system table (had viaje + openclaw rows)
safe('old sys table', lambda: archive('32e0a0b1-97cc-81aa-8735-c8fde94a15a4'))
# 4. "Archivo temporal" heading
safe('archivo temporal heading', lambda: archive('32f0a0b1-97cc-81cf-9412-f08f278dad47'))
# 5. "Archivo temporal" paragraph
safe('archivo temporal para', lambda: archive('32f0a0b1-97cc-81a3-9662-d9082113af26'))
# 6. Trailing divider after archivo temporal
safe('trailing divider', lambda: archive('32f0a0b1-97cc-814d-86b8-f2a5838c0f8d'))

print('Final cleanup done.')
