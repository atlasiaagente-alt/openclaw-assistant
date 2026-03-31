# Atlas Delivery Validation

## Objetivo
Evitar falsos positivos de cierre cuando una tarea depende de salida a canal externo o cambio visible en un sistema.

## Regla central
- coordinado != ejecutado
- ejecutado != entregado
- entregado != cerrado

## Definiciones
### Coordinado
La tarea fue hablada, asignada o instruida internamente.
No cuenta como progreso suficiente para marcar done.

### Ejecutado
El agente realizó una acción interna o intentó una acción.
Tampoco basta si la tarea dependía de resultado externo.

### Entregado
La acción salió realmente al canal externo correcto o produjo el cambio esperado en el sistema correcto.

### Cerrado
Solo cuando la entrega o resultado fue validado con evidencia suficiente.

## Cuándo aplicar esta validación
Aplicar siempre que haya:
- mensajes por WhatsApp u otro canal externo
- cambios en Notion
- cambios en sistemas de trabajo
- envíos a correo o calendario
- cualquier salida que no deba asumirse por simple intención o coordinación interna

## Evidencias válidas
- confirmación de salida real por el canal nativo
- cambio visible en el sistema objetivo
- ID, link o registro verificable
- respuesta observable que confirme recepción cuando aplique

## Evidencias no suficientes por sí solas
- "ya lo hice"
- coordinación entre sesiones
- intención declarada
- resumen sin prueba
- ejecución interna sin salida real

## Secuencia operativa
1. Atlas delega.
2. El agente coordina o ejecuta.
3. Atlas verifica si hubo entrega real.
4. Si no hay entrega real, no usar closed.
5. Si hay entrega pero falta validación final, usar delivered.
6. Solo después usar closed.

## Estados sugeridos
- delegated
- in_progress
- waiting
- delivered
- closed
- blocked
- escalated

## Regla por canal
### WhatsApp y mensajería externa
No marcar como hecho solo por sessions_send o coordinación interna.
Debe existir evidencia de salida real por la vía nativa correspondiente.

### Notion
No marcar como hecho sin verificar que el bloque, página o propiedad cambió de verdad.

### Correo / calendario
No marcar como hecho sin confirmación del envío o creación real.

## Regla final
Si hay duda sobre entrega, el estado correcto no es closed.
El estado correcto es waiting, blocked o delivered pendiente de validación.
