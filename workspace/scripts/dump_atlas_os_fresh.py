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


def get_children(block_id):
    return notion('GET', f'https://api.notion.com/v1/blocks/{block_id}/children?page_size=100')


def extract_text(rich_text_arr):
    if not rich_text_arr:
        return ''
    return ''.join(t.get('plain_text', '') for t in rich_text_arr)


def read_block(b):
    btype = b.get('type', '')
    data = b.get(btype, {})
    text = extract_text(data.get('rich_text', []))
    return btype, text, b['id']


def print_table_rows(block_id, indent='  '):
    try:
        rows_resp = get_children(block_id)
        for row in rows_resp.get('results', []):
            cells = row.get('table_row', {}).get('cells', [])
            cell_texts = ['|'.join(extract_text(c) for c in cells) if isinstance(cells[0], list) else '']
            # cells is list of list of rich_text
            row_text = ' | '.join(
                ''.join(t.get('plain_text', '') for t in cell)
                for cell in cells
            )
            print(f'{indent}  ROW: {row_text[:120]}')
    except Exception as e:
        print(f'{indent}  (error reading rows: {e})')


top = get_children(PAGE_ID)
for b in top.get('results', []):
    btype, text, bid = read_block(b)
    label = f'[{btype}]'
    if btype == 'table':
        print(f'{label} (table id={bid})')
        print_table_rows(bid)
    elif btype in ('child_database',):
        title = b.get('child_database', {}).get('title', '')
        print(f'{label} DB: {title}')
    elif btype == 'child_page':
        title = b.get('child_page', {}).get('title', '')
        print(f'{label} PAGE: {title}')
    elif btype == 'toggle':
        print(f'{label} {text}')
    elif btype == 'divider':
        print('---')
    elif text:
        print(f'{label} {text}')
    else:
        print(f'{label} (empty)')
