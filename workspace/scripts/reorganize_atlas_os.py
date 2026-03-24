import json
import os
import urllib.request

TOKEN = os.environ.get('NOTION_TOKEN')
PAGE_ID = '3290a0b1-97cc-801a-8240-e78d3bfe0e74'

if not TOKEN:
    raise SystemExit('NOTION_TOKEN missing')

headers = {
    'Authorization': f'Bearer {TOKEN}',
    'Notion-Version': '2022-06-28',
    'Content-Type': 'application/json',
}

def text(content):
    return {'type': 'text', 'text': {'content': content}}

def req(method, url, payload=None):
    data = None if payload is None else json.dumps(payload).encode('utf-8')
    request = urllib.request.Request(url, data=data, method=method)
    for k, v in headers.items():
        request.add_header(k, v)
    with urllib.request.urlopen(request) as resp:
        return json.loads(resp.read().decode('utf-8'))

children = [
    {'object': 'block', 'type': 'divider', 'divider': {}},
    {'object': 'block', 'type': 'heading_2', 'heading_2': {'rich_text': [text('Dashboard operativo')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'paragraph', 'paragraph': {'rich_text': [text('Vista pensada para decidir rapido: que importa hoy, que esta en movimiento, donde hay bloqueo y que sigue.')], 'color': 'default'}},
    {'object': 'block', 'type': 'callout', 'callout': {'rich_text': [text('Uso simple: captura en tablas base, mira el foco, ejecuta y revisa bloqueos.')], 'color': 'gray_background', 'icon': {'type': 'emoji', 'emoji': '📌'}}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Foco de hoy')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'to_do', 'to_do': {'rich_text': [text('1 resultado clave del dia')], 'checked': False, 'color': 'default'}},
    {'object': 'block', 'type': 'to_do', 'to_do': {'rich_text': [text('1 bloqueo a resolver hoy')], 'checked': False, 'color': 'default'}},
    {'object': 'block', 'type': 'to_do', 'to_do': {'rich_text': [text('1 siguiente paso concreto')], 'checked': False, 'color': 'default'}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Panel de decision')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Ahora: lo que esta activo y merece atencion inmediata.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Siguiente: cola corta de lo proximo en entrar.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Bloqueos: cosas detenidas por dependencia, decision o energia.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Delegado: que esta en manos de Atlas, Hestia, Prometeo o Ares.')], 'color': 'default'}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Ritmo semanal')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'numbered_list_item', 'numbered_list_item': {'rich_text': [text('Lunes a miercoles: empuje de produccion y negocio.')], 'color': 'default'}},
    {'object': 'block', 'type': 'numbered_list_item', 'numbered_list_item': {'rich_text': [text('Jueves a domingo: entrenamiento, vida personal y mantenimiento.')], 'color': 'default'}},
    {'object': 'block', 'type': 'numbered_list_item', 'numbered_list_item': {'rich_text': [text('Revisiones: 8:00 AM y 7:00 PM para correo, calendario y prioridades.')], 'color': 'default'}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Agentes y duenos')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Atlas -> router, agenda, email y coordinacion general.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Prometeo -> TradeLab, MVP y desbloqueo tecnico.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Ares -> entrenamiento, disciplina y carga semanal.')], 'color': 'default'}},
    {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Hestia -> hogar y coordinacion domestica.')], 'color': 'default'}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Reglas del tablero')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'toggle', 'toggle': {'rich_text': [text('Estados recomendados')], 'color': 'default', 'children': [
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Inbox -> entro pero aun no se decide.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Definir -> requiere aclarar alcance o criterio.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Listo -> listo para ejecutar.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('En progreso -> ya se esta haciendo.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('En espera o Bloqueado -> detenido por alguien o algo.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Hecho -> cerrado y fuera del foco.')], 'color': 'default'}},
    ]}},
    {'object': 'block', 'type': 'toggle', 'toggle': {'rich_text': [text('Prioridad recomendada')], 'color': 'default', 'children': [
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Alta -> mueve resultado o evita dano.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Media -> importante pero no urgente.')], 'color': 'default'}},
        {'object': 'block', 'type': 'bulleted_list_item', 'bulleted_list_item': {'rich_text': [text('Baja -> mantenimiento o nice to have.')], 'color': 'default'}},
    ]}},
    {'object': 'block', 'type': 'heading_3', 'heading_3': {'rich_text': [text('Plantilla rapida de captura')], 'color': 'default', 'is_toggleable': False}},
    {'object': 'block', 'type': 'quote', 'quote': {'rich_text': [text('[Area] | [Resultado esperado] | [Responsable] | [Estado] | [Prioridad] | [Siguiente paso]')], 'color': 'default'}},
]

resp = req('PATCH', f'https://api.notion.com/v1/blocks/{PAGE_ID}/children', {'children': children})
print(json.dumps(resp, ensure_ascii=False, indent=2))
