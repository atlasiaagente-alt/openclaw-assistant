import json, os, urllib.request
TOKEN=os.environ['NOTION_TOKEN']
HEADERS={'Authorization':'Bearer '+TOKEN,'Notion-Version':'2025-09-03','Content-Type':'application/json'}

def notion(method, url, payload=None):
    data=None if payload is None else json.dumps(payload).encode('utf-8')
    req=urllib.request.Request(url, data=data, method=method, headers=HEADERS)
    with urllib.request.urlopen(req) as resp:
        body=resp.read().decode('utf-8')
        return json.loads(body) if body else {}

def text_cell(content):
    return [{"type":"text","text":{"content":content}}]

def replace_row(row_id, cells):
    return notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', {'table_row': {'cells': [text_cell(c) for c in cells]}})

updates = {
    '32e0a0b1-97cc-814f-9ddb-f6d7f844458b': [
        'Validar Paddle webhook','En progreso coordinado','TradeLab','Alta','Alto','Payments',
        'Prometeo confirmo que esta linea va primero y absorbe la validacion de pagos Paddle. Primer paso definido previamente: revisar handler/ruta actual del webhook, firma/secreto y actualizacion del estado de pago. En la revision de hoy 8:00 AM no respondio a dos pings de seguimiento, asi que sigue coordinado pero sin ejecucion confirmada; queda pendiente/escalado, no resuelto.'
    ],
    '32e0a0b1-97cc-81bc-a0ae-e8d23fc2da0c': [
        'Comprar mercado','Pendiente hoy','Hogar','Media','','Hestia habia definido como siguiente paso revisar faltantes y dejar cerrada la lista de compra. En la revision de hoy 8:00 AM no respondio a dos pings de seguimiento, asi que la tarea sigue coordinada pero no ejecutada; pendiente de retomar o escalar si sigue muda.'
    ],
    '32e0a0b1-97cc-8126-baae-cb00c02f06fa': [
        'Comprar agua segun tablero','Waiting','Hogar','Media','','Hestia habia dejado como destrabe seguro preguntar a Jorge si ya hace falta pedir el agua. En la revision de hoy 8:00 AM no respondio a dos pings de seguimiento, asi que el bloqueo sigue explicito y sin ejecucion confirmada.'
    ],
    '32e0a0b1-97cc-8184-b75c-fda2f5ee1925': [
        'Entrenamiento de pecho manana 5AM 26/abril/2026','Bloqueado','Media','Media',
        'Ares ya habia marcado inconsistencia de fecha/tarea; no se debe ejecutar ni avisar nada hasta corregirla. En la revision de hoy 8:00 AM no respondio a dos pings pidiendo decision final, asi que se mantiene bloqueado y escalado; no coordinado como resuelto.'
    ],
    '32e0a0b1-97cc-815e-a3b2-e56cb41f4978': [
        'Pedir fotos para el grupo de smart project','Bloqueado','Entrenamiento','Media',
        'Ares habia definido que el destrabe seguro es pedir confirmacion minima de quien debe enviar las fotos y en que canal exacto debe salir la solicitud. En la revision de hoy 8:00 AM no respondio a dos pings, asi que el bloqueo sigue explicito y pendiente de destrabe externo o respuesta posterior.'
    ],
}

for row_id, cells in updates.items():
    replace_row(row_id, cells)
    print('updated', row_id)
