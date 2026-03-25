import json, os, sys, urllib.request

TOKEN = os.environ.get('NOTION_TOKEN')
if not TOKEN:
    raise SystemExit('NOTION_TOKEN missing')

HEADERS = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2025-09-03',
    'Content-Type': 'application/json',
}


def notion(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        body = resp.read().decode('utf-8')
        return json.loads(body) if body else {}


def rich_text_plain(rt):
    if not rt:
        return ''
    out = []
    for item in rt:
        t = item.get('plain_text')
        if t:
            out.append(t)
    return ''.join(out).strip()


def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]


def list_rows(table_id):
    rows = notion('GET', f'https://api.notion.com/v1/blocks/{table_id}/children?page_size=100').get('results', [])
    out = []
    for r in rows:
        if r.get('type') != 'table_row':
            continue
        cells = []
        for cell in (r.get('table_row') or {}).get('cells', []):
            cells.append(rich_text_plain(cell))
        out.append({'id': r.get('id'), 'cells': cells})
    return out


def append_row(table_id, cells):
    payload = {
        'children': [{
            'object': 'block',
            'type': 'table_row',
            'table_row': {'cells': [text_cell(c) for c in cells]}
        }]
    }
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{table_id}/children', payload)


def replace_row(row_id, cells):
    payload = {
        'table_row': {'cells': [text_cell(c) for c in cells]}
    }
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', payload)


cmd = sys.argv[1]
if cmd == 'list':
    table_id = sys.argv[2]
    print(json.dumps(list_rows(table_id), ensure_ascii=True, indent=2))
elif cmd == 'append':
    table_id = sys.argv[2]
    cells = json.loads(sys.argv[3])
    print(json.dumps(append_row(table_id, cells), ensure_ascii=True, indent=2))
elif cmd == 'replace':
    row_id = sys.argv[2]
    cells = json.loads(sys.argv[3])
    print(json.dumps(replace_row(row_id, cells), ensure_ascii=True, indent=2))
else:
    raise SystemExit('usage: list <table_id> | append <table_id> <json_cells> | replace <row_id> <json_cells>')
