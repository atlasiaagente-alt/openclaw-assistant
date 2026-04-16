import json, os, urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
TOKEN = os.environ['NOTION_TOKEN']
DS = '32f0a0b1-97cc-8185-b332-000b7592f8b3'
HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
body = {'page_size': 100}
req = urllib.request.Request(f'https://api.notion.com/v1/data_sources/{DS}/query', data=json.dumps(body).encode('utf-8'), method='POST', headers=HEADERS)
with urllib.request.urlopen(req) as resp:
    print(resp.read().decode('utf-8'))
