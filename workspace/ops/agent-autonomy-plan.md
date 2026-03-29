# Plan corto — agentes más autónomos, interactivos y productivos

Fecha: 2026-03-27

## Problema actual
Hay tareas en tracker que quedan vivas pero no siempre avanzan a:
- decisión clara
- primer paso ejecutado
- bloqueo explícito
- actualización honesta de estado

## Objetivo
Pasar de agentes "reactivos" a agentes que:
1. se hablen entre sí cuando toca
2. dejen evidencia real
3. escalen rápido bloqueos
4. mantengan el tracker honesto

## Cambios propuestos
### 1) Regla de salida mínima por tarea
Cada agente debe responder con uno de estos formatos:
- **DECISIÓN:** qué hará
- **PRIMER PASO:** acción concreta inmediata
- **BLOQUEO:** qué falta exactamente

### 2) Tracker como fuente de verdad
Nunca dejar tareas activas sin mover el estado real:
- Backlog
- Next
- In progress
- Waiting
- Blocked
- Done

### 3) Escalada más agresiva
Si un agente no responde o responde ambiguo:
- se reintenta una vez con instrucción más cerrada
- si sigue ambiguo, Atlas actualiza a `Blocked` o `Waiting` según evidencia
- Atlas deja siguiente acción explícita

### 4) Más conversación entre agentes
Usar handoffs concretos, por ejemplo:
- Prometeo -> Atlas: bloqueo técnico o decisión de producto
- Hestia -> Atlas: falta confirmación humana o canal externo
- Ares -> Atlas: inconsistencia de fechas/rutina/destino

### 5) Definición de “Done” más dura
Solo `Done` cuando exista evidencia real de entrega:
- mensaje enviado
- archivo creado
- cambio aplicado
- resultado verificado

## Primer experimento
Aplicar esta política en la revisión de Atlas OS durante 3-5 días y mirar si:
- bajan tareas ambiguas
- suben notas útiles
- se reduce backlog zombie
