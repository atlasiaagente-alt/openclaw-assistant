import json
import os
import sys
import urllib.request

sys.stdout.reconfigure(encoding='utf-8')

TOKEN = os.environ['NOTION_TOKEN']
DB = '32f0a0b1-97cc-81a8-9443-df3f85f2ffc7'
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

req = urllib.request.Request(
    f'https://api.notion.com/v1/databases/{DB}/query',
    data=json.dumps({'page_size': 100}).encode('utf-8'),
    method='POST',
    headers=HEADERS,
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))


def text_value(prop):
    if not prop:
        return ''
    typ = prop.get('type')
    if typ in ('rich_text', 'title'):
        return ''.join(item.get('plain_text', '') for item in prop.get(typ, []))
    if typ == 'status':
        return (prop.get('status') or {}).get('name', '')
    if typ == 'select':
        return (prop.get('select') or {}).get('name', '')
    if typ == 'date':
        return (prop.get('date') or {}).get('start', '')
    if typ == 'checkbox':
        return prop.get('checkbox', False)
    return ''

fields = ['Task name', 'Owner', 'Status', 'Priority', 'Area', 'Next step', 'Notes', 'Source', 'Evidence / brief', 'Next check', 'Needs Gustavo']
rows = []
for result in data['results']:
    props = result['properties']
    row = {field: text_value(props.get(field)) for field in fields}
    row['created_time'] = result.get('created_time', '')
    row['last_edited_time'] = result.get('last_edited_time', '')
    rows.append(row)

for row in rows:
    if row['Status'] != 'Done':
        print(json.dumps(row, ensure_ascii=False))
