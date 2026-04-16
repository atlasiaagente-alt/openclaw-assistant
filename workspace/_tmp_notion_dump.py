import json, os, urllib.request
DB='32f0a0b1-97cc-81a8-9443-df3f85f2ffc7'
headers={'Authorization':'Bearer '+os.environ['NOTION_TOKEN'],'Notion-Version':'2022-06-28','Content-Type':'application/json'}
payload=json.dumps({'page_size':100}).encode()
req=urllib.request.Request(f'https://api.notion.com/v1/databases/{DB}/query', data=payload, headers=headers, method='POST')
data=json.load(urllib.request.urlopen(req))

def plain(prop):
    t=prop['type']
    if t=='title': return ''.join(x.get('plain_text','') for x in prop['title'])
    if t=='rich_text': return ''.join(x.get('plain_text','') for x in prop['rich_text'])
    if t in ('select','status'):
        v=prop[t]
        return v.get('name') if v else None
    if t=='people': return [x.get('name') for x in prop['people']]
    if t=='date': return (prop['date'] or {}).get('start') if prop['date'] else None
    if t in ('last_edited_time','created_time'): return prop[t]
    if t=='formula':
        f=prop['formula']; return f.get(f['type'])
    if t=='checkbox': return prop['checkbox']
    return None
rows=[]
for page in data['results']:
    row={k:plain(v) for k,v in page['properties'].items()}
    row['id']=page['id']
    rows.append(row)
with open('_tmp_notion_rows.json','w',encoding='utf-8') as f:
    json.dump(rows,f,ensure_ascii=False,indent=2)
print('wrote', len(rows))
