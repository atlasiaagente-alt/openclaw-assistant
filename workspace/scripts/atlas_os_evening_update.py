import json, os, urllib.request

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

def text_cell(content):
    return [{"type": "text", "text": {"content": content}}]

def replace_row(row_id, cells):
    payload = {'table_row': {'cells': [text_cell(c) for c in cells]}}
    notion('PATCH', f'https://api.notion.com/v1/blocks/{row_id}', payload)

updates = {
    '3290a0b1-97cc-8037-8aeb-e58c39cfded8': [
        'Validar pagos Paddle','En progreso coordinado','Payment','Alta','Alto','Payments',
        'Prometeo respondio que arranca primero y que esta fila se unifica con Validar Paddle webhook como misma linea operativa. Primer paso: revisar handler/config del webhook y el flujo de actualizacion de pago. Sin bloqueo declarado. En el cierre del dia no respondio al nuevo ping; sigue coordinado, no ejecutado ni entregado.'
    ],
    '3290a0b1-97cc-80f9-9c0f-fe9bf7933665': [
        'Comprar dominio','Waiting coordinacion','Infra','Alta','Alto','Infra',
        'Prometeo definio dejarla en segundo lugar despues de pagos. Primer paso: confirmar dominio final y proveedor para compra. Bloqueo declarado: falta decision final del dominio si no esta cerrada. En el cierre del dia no respondio al nuevo ping; sigue coordinado, no ejecutado.'
    ],
    '3290a0b1-97cc-803f-a3ed-fc1a2d5d50ff': [
        'Ajustar UI dashboard','Waiting coordinacion','Feature','Media','Medio','Frontend',
        'Prometeo la dejo despues de pagos y dominio. Primer paso: definir el ajuste puntual de mayor impacto y acotarlo a un cambio pequeno. Bloqueo declarado: falta definir que ajuste entra primero. En el cierre del dia no respondio al nuevo ping; sigue coordinado, no ejecutado.'
    ],
    '32e0a0b1-97cc-814f-9ddb-f6d7f844458b': [
        'Validar Paddle webhook','En progreso coordinado','TradeLab','Alta','Alto','Payments',
        'Prometeo confirmo que esta linea va primero y absorbe la validacion de pagos Paddle. Primer paso: revisar handler/ruta actual del webhook, firma/secreto y actualizacion del estado de pago. Sin bloqueo declarado. Coordinado, no ejecutado ni entregado.'
    ],
    '32e0a0b1-97cc-81bc-a0ae-e8d23fc2da0c': [
        'Comprar mercado','Pendiente hoy','Hogar','Media','','Hestia reporto estado pendiente. Siguiente paso concreto hoy: revisar faltantes y dejar cerrada la lista de compra. Sin bloqueo declarado. Coordinado, no ejecutado.'
    ],
    '32e0a0b1-97cc-8126-baae-cb00c02f06fa': [
        'Comprar agua segun tablero','Waiting','Hogar','Media','','Hestia reporto estado pendiente en espera. Bloqueo: depende de confirmacion de Jorge. Accion segura propuesta para destrabar: preguntarle si ya hace falta pedir el agua. Coordinado, no ejecutado.'
    ],
    '32e0a0b1-97cc-8184-b75c-fda2f5ee1925': [
        'Entrenamiento de pecho manana 5AM 26/abril/2026','Bloqueado','Media','Media',
        'Ares mantiene que no debe ejecutarse por inconsistencia de fecha/tarea; ademas su respuesta previa menciona 25/abril mientras la fila actual dice 26/abril, asi que la inconsistencia sigue viva. Primer paso: confirmar rutina y fecha real antes de avisar o mover nada. Coordinado, no ejecutado.'
    ],
    '32e0a0b1-97cc-815e-a3b2-e56cb41f4978': [
        'Pedir fotos para el grupo de smart project','Bloqueado','Entrenamiento','Media',
        'Ares definio que el destrabe seguro es pedir confirmacion minima de quien debe enviar las fotos y en que canal exacto debe salir la solicitud. Bloqueo declarado: falta persona responsable y canal exacto. En el cierre del dia no respondio al nuevo ping; sigue coordinado, no ejecutado.'
    ],
}

for row_id, cells in updates.items():
    replace_row(row_id, cells)
    print(f'updated {row_id}')
