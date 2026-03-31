# Atlas Short Ops Board

## Objetivo
Dar a Atlas una vista de control corta y útil para gobernar el sistema sin releer todo el contexto cada vez.

## Regla base
El tablero operativo no es archivo histórico.
Es una vista viva para decidir qué mover ahora.

## Secciones mínimas
- Inbox
- En curso
- Waiting
- Bloqueados
- Decisiones de Gustavo
- Cerrado reciente

## Qué entra en cada sección

### Inbox
- señales nuevas sin triage completo
- tareas nuevas aún sin owner definitivo

### En curso
- tareas activas con owner claro
- trabajo ya empujado y en movimiento

### Waiting
- tareas esperando respuesta externa
- tareas delegadas pendientes de ejecución o confirmación

### Bloqueados
- tareas detenidas por falta de info, conflicto o dependencia dura

### Decisiones de Gustavo
- solo lo que realmente requiere criterio humano
- no usar esta sección para pereza operativa de Atlas

### Cerrado reciente
- últimos cierres verificados para contexto corto y seguimiento

## Campos recomendados por item
- Tarea
- Owner
- Área
- Estado
- Próximo paso
- Próximo check
- Evidencia o nota breve

## Reglas de uso
- Si algo no tiene owner, no puede quedarse mucho tiempo fuera de Inbox.
- Si algo depende de respuesta, no va a En curso: va a Waiting.
- Si algo requiere decisión humana real, va a Decisiones de Gustavo.
- Si algo se cerró sin evidencia suficiente, no va a Cerrado reciente.

## Prioridad de lectura diaria
Atlas debe leer en este orden:
1. Bloqueados
2. Waiting
3. Decisiones de Gustavo
4. En curso
5. Inbox
6. Cerrado reciente

## Regla de compactación
El tablero debe mantenerse corto.
Si una tarea necesita historial largo, ese historial vive en otra parte; aquí queda solo el estado operativo actual.

## Resultado esperado
Atlas debe poder abrir este tablero y responder en menos de un minuto:
- qué está pendiente
- qué está bloqueado
- qué requiere reempuje
- qué necesita decisión humana
- qué se cerró de verdad
