# Security baseline notes for all agents

Basado en la guía de seguridad de OpenClaw (`docs.openclaw.ai/gateway/security`) y adaptado al uso de Gustavo.

## Principio base

- OpenClaw debe tratarse como **asistente personal** dentro de **un único límite de confianza** por gateway.
- No asumir aislamiento fuerte multi-tenant entre usuarios adversariales dentro del mismo gateway.
- Si en el futuro hay límites de confianza distintos, separar por gateway/host/OS user.

## Reglas operativas para todos los agentes

- Mantener mínimo privilegio por defecto.
- No abrir accesos o canales innecesarios.
- No asumir que aislamiento de sesión equivale a autorización real.
- Evitar mezclar agentes personales con contextos de terceros sin reglas claras.
- Si un agente habla con múltiples personas, recordar que comparten la autoridad de herramientas de ese agente si esas herramientas están permitidas.

## Canales / mensajería

- Preferir `dmPolicy: pairing` o allowlists estrictas.
- Mantener `session.dmScope: per-channel-peer` para aislar DMs por contacto.
- En grupos, requerir mención cuando sea posible.
- No exponer agentes con herramientas potentes a grupos o audiencias abiertas.

## Herramientas

- Usar el menor set de herramientas necesario.
- Evitar permisos elevados por defecto.
- No asumir que prompt guardrails sustituyen aislamiento real.
- Para agentes de terceros o entornos más sensibles, reducir herramientas antes de ampliar acceso.

## Gateway / runtime

- Mantener gateway en modo local/loopback cuando no haya necesidad real de exposición.
- Tratar acceso autenticado al gateway como acceso de operador confiable.
- Recordar que `sessionKey` enruta contexto; no es frontera de autorización.

## Patrón para futuros agentes

Antes de dar acceso a canales o herramientas a un agente nuevo:

1. definir su rol y límite de confianza
2. minimizar herramientas
3. confirmar routing/canales necesarios
4. aislar workspace/agentId
5. evitar exposición abierta innecesaria

## Nota

Estas notas son criterio operativo interno; no sustituyen revisar la documentación de seguridad cuando se hagan cambios sensibles de gateway, canales, nodos o permisos.
