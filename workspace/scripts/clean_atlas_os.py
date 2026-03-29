import json, os, sys, urllib.request, urllib.error
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN = os.environ['NOTION_TOKEN']
VERSION = '2025-09-03'
PAGE_ID = '3290a0b1-97cc-801a-8240-e78d3bfe0e74'
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


def delete_block(block_id):
    return notion('DELETE', f'https://api.notion.com/v1/blocks/{block_id}')


def get_children(block_id):
    return notion('GET', f'https://api.notion.com/v1/blocks/{block_id}/children?page_size=100')


def extract_text(rich_text_arr):
    if not rich_text_arr:
        return ''
    return ''.join(t.get('plain_text', '') for t in rich_text_arr)


# Step 1: Get all top-level blocks and identify which to archive
print('=== Fetching all top-level blocks ===')
top = get_children(PAGE_ID)
blocks = []
for b in top.get('results', []):
    btype = b.get('type', '')
    data = b.get(btype, {})
    text = extract_text(data.get('rich_text', []))
    blocks.append({'id': b['id'], 'type': btype, 'text': text})

# The clean structure starts at heading_1 "Atlas OS" 
# Everything before that is the old messy version that should be archived
# Find the heading_1 "Atlas OS" block
atlas_os_idx = None
for i, bl in enumerate(blocks):
    if bl['type'] == 'heading_1' and 'Atlas OS' in bl['text']:
        atlas_os_idx = i
        break

if atlas_os_idx is None:
    print('ERROR: Could not find heading_1 Atlas OS')
    sys.exit(1)

print(f'Found "Atlas OS" heading at index {atlas_os_idx} of {len(blocks)} blocks')
print(f'Will archive {atlas_os_idx} blocks above it (old structure)')

# Archive everything ABOVE the Atlas OS heading (indices 0 to atlas_os_idx-1)
for i in range(atlas_os_idx):
    bl = blocks[i]
    # Skip child_database (Tasks Tracker) - that's valuable
    if bl['type'] == 'child_database':
        print(f'SKIP (keep DB): [{bl["type"]}] {bl["text"][:60]}')
        continue
    safe(f'archive [{bl["type"]}] {bl["text"][:50]}', lambda bid=bl['id']: archive(bid))

# Step 2: Archive duplicate rows in Hestia table
# Hestia table: 3290a0b1-97cc-805a-ae65-f2f0f9981c2b
# Last row is a duplicate of "Comprar agua segun tablero"
print('\n=== Fixing Hestia duplicates ===')
hestia = get_children('3290a0b1-97cc-805a-ae65-f2f0f9981c2b')
hestia_rows = hestia.get('results', [])
seen_tasks = set()
for row in hestia_rows:
    cells = row.get('table_row', {}).get('cells', [])
    if cells:
        task_name = ''.join(t.get('plain_text', '') for t in cells[0])
        if task_name in seen_tasks and task_name:
            safe(f'archive hestia dup "{task_name[:40]}"', lambda rid=row['id']: archive(rid))
        else:
            seen_tasks.add(task_name)

# Step 3: Archive duplicate rows in Ares table
# Ares table: 3290a0b1-97cc-80f4-98f8-cd4e17258a55
print('\n=== Fixing Ares duplicates ===')
ares = get_children('3290a0b1-97cc-80f4-98f8-cd4e17258a55')
ares_rows = ares.get('results', [])
seen_tasks = set()
for row in ares_rows:
    cells = row.get('table_row', {}).get('cells', [])
    if cells:
        task_name = ''.join(t.get('plain_text', '') for t in cells[0])
        if task_name in seen_tasks and task_name:
            safe(f'archive ares dup "{task_name[:40]}"', lambda rid=row['id']: archive(rid))
        else:
            seen_tasks.add(task_name)

# Step 4: Also archive the "Archivo temporal" heading and trailing divider that's below the clean section
# These are after the clean block and add noise
print('\n=== Checking for trailing noise below clean section ===')
for i in range(atlas_os_idx, len(blocks)):
    bl = blocks[i]
    if 'Archivo temporal' in bl['text']:
        safe(f'archive trailing "{bl["text"][:50]}"', lambda bid=bl['id']: archive(bid))
    # Also archive the trailing divider right after it
    if bl['type'] == 'divider' and i > atlas_os_idx + 15:
        safe(f'archive trailing divider', lambda bid=bl['id']: archive(bid))

print('\nDone cleaning.')
