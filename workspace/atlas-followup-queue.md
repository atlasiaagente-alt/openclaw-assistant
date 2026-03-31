# Atlas Follow-up Queue

## Objetivo
Evitar que las delegaciones se pierdan. Toda tarea delegada debe quedar registrada hasta que:
- se cierre
- se bloquee
- o se escale

## Regla base
Delegar no cierra el trabajo.
Atlas sigue siendo dueño del seguimiento hasta tener cierre verificable.

## Formato de registro
Cada entrada debe incluir:
- ID
- Fecha
- Owner
- Tarea
- Canal
- Estado
- Espera de qué
- Próximo check
- Evidencia
- Resultado

## Estados válidos
- delegated
- in_progress
- waiting
- blocked
- delivered
- closed
- escalated

## Plantilla de entrada

- ID: FQ-YYYYMMDD-01
- Fecha: 
- Owner: 
- Tarea: 
- Canal: 
- Estado: delegated
- Espera de qué: 
- Próximo check: 
- Evidencia: 
- Resultado: 

## Uso operativo
1. Si Atlas delega, crea entrada.
2. Si el agente responde pero no ejecuta, mover a waiting o blocked, no a closed.
3. Si hay entrega real, mover a delivered.
4. Si el ciclo terminó y quedó validado, mover a closed.
5. Si requiere decisión humana, mover a escalated.

## Criterio de revisión
Revisar primero:
- waiting antiguos
- blocked sin movimiento
- delegated sin respuesta
- delivered pendientes de validación final

## Regla de higiene
- No dejar entradas sin próximo check si siguen abiertas.
- No usar closed sin evidencia suficiente.
- Si una tarea depende de canal externo, delivered va antes de closed.

## Vista mínima recomendada
Operar esta cola como lista corta de control, no como archivo muerto.
La prioridad diaria es:
- qué está esperando
- qué está bloqueado
- qué necesita reempuje
