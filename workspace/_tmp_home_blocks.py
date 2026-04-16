import json
import os
import urllib.request
import urllib.error
import sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TOKEN = os.environ['NOTION_TOKEN']
PAGE = '32f0a0b1-97cc-8115-9e62-ec8765ad533c'
HEADERS = {
    'Authorization': 'Bearer ' + TOKEN,
    'Notion-Version': '2025-09-03',
    'Content-Type': 'application/json',
}

req = urllib.request.Request(
    f'https://api.notion.com/v1/blocks/{PAGE}/children?page_size=100',
    headers=HEADERS,
    method='GET'
)

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode('utf-8'))
print(json.dumps(data, ensure_ascii=False, indent=2))
