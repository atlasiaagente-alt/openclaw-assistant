import json
import os
import urllib.request

TOKEN = os.environ['NOTION_TOKEN']
DB = '32f0a0b1-97cc-81a8-9443-df3f85f2ffc7'
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': '2025-09-03',
    'Content-Type': 'application/json',
}

req = urllib.request.Request(
    f'https://api.notion.com/v1/databases/{DB}/query',
    data=json.dumps({'page_size': 100}).encode('utf-8'),
    method='POST',
    headers=HEADERS,
)

try:
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
    print(json.dumps(data, ensure_ascii=False, indent=2))
except urllib.error.HTTPError as e:
    body = e.read().decode('utf-8', errors='replace')
    print('HTTP', e.code)
    print(body)
