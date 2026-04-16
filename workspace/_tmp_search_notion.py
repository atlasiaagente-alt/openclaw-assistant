import json, os, urllib.request, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
TOKEN = os.environ['NOTION_TOKEN']
HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Notion-Version': '2025-09-03', 'Content-Type': 'application/json'}
body = {'query': 'Tasks Tracker'}
req = urllib.request.Request('https://api.notion.com/v1/search', data=json.dumps(body).encode('utf-8'), method='POST', headers=HEADERS)
with urllib.request.urlopen(req) as resp:
    print(resp.read().decode('utf-8'))
