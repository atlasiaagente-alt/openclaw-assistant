# Playbook - Varios agentes en un mismo WhatsApp compartido

Objetivo: replicar el patrón que funcionó con **Hestia** y **Ares** usando **un solo número / una sola sesión de WhatsApp**, pero enroutando contactos o grupos distintos a agentes distintos.

## Idea base

No hace falta un WhatsApp aparte por agente.
Sí hace falta:

- un agente aislado por rol
- bindings por contacto o grupo hacia el `agentId` correcto
- copiar auth del canal cuando haga falta
- ajustar la activación en grupos para que el agente despierte de forma usable

## Qué sí funcionó

### 1) Un mismo WhatsApp para múltiples agentes

Patrón válido:
- mismo canal de WhatsApp
- misma cuenta enlazada
- múltiples agentes aislados por dentro
- routing por peer/grupo hacia cada agente

Casos ya probados:
- **Hestia** ← WhatsApp directo de Jorge
- **Ares** ← grupo de WhatsApp `Smart Project`

## 2) Binding por contacto directo

Para contactos tipo DM/directo, funcionó este patrón conceptual:

- binding de `whatsapp`
- `peer.kind = direct`
- `peer.id = +E164`

Ejemplo real:
- Jorge (`+573144752380`) → `hestia`

## 3) Binding por grupo

Para grupos, funcionó este patrón conceptual:

- binding de `whatsapp`
- `peer.kind = group`
- `peer.id = <group-jid>`

Ejemplo real:
- `120363424964463765@g.us` → `ares`

## 4) El grupo puede enrutar bien y aun así no responder

Esto fue importante.

Aunque el binding del grupo hacia `ares` ya estaba bien, Ares no respondió al principio.
La causa no era el routing sino el **mention gating** del grupo de WhatsApp.

En logs aparecía:
- inbound correcto del grupo
- `wasMentioned: false`

Eso significa:
- el mensaje sí llegó
- el grupo sí estaba asociado al agente
- pero OpenClaw no despertaba respuesta automática porque no detectaba una mención válida

## 5) Qué lo resolvió

Lo que sí funcionó fue configurar `groupChat.mentionPatterns` dentro del agente en `agents.list[]`.

En el caso de `ares`, se añadió una configuración equivalente a esta:

```json
{
  "id": "ares",
  "groupChat": {
    "historyLimit": 50,
    "mentionPatterns": [
      "\\bares\\b",
      "\\bAres\\b"
    ]
  }
}
```

Con eso, escribir `Ares ...` en el grupo ya sirvió como activación textual usable, sin depender de una mención técnica real de WhatsApp.

## Regla práctica para futuros agentes de grupo

Si un agente va a vivir en grupos de WhatsApp compartidos, no basta con:
- crear el agente
- bindear el grupo

También conviene definir:
- `groupChat.mentionPatterns`

Si no, el grupo puede enrutar al agente pero quedarse silencioso porque el sistema no considera que lo mencionaron.

## Pasos replicables

### Caso A: agente para contacto directo

1. crear el agente aislado
2. copiar/auth si hace falta
3. personalizar `IDENTITY.md`, `USER.md`, `SOUL.md`
4. agregar binding directo por número
5. probar con mensaje real
6. guardar reglas operativas del contacto en memoria

### Caso B: agente para grupo

1. crear el agente aislado
2. copiar/auth si hace falta
3. personalizar `IDENTITY.md`, `USER.md`, `SOUL.md`
4. identificar el `group-jid`
5. agregar binding del grupo hacia el agente
6. definir `groupChat.mentionPatterns` en `agents.list[]`
7. recargar o reiniciar gateway si aplica
8. probar con mensaje real en el grupo usando el nombre textual del agente
9. revisar logs si no responde

## Señales de diagnóstico útiles

### Si el binding no existe
Verás que el tráfico sigue cayendo en `main` o en otro agente.

### Si el binding existe pero no responde
Revisar logs.
Si aparece:
- `wasMentioned: false`

y el mensaje sí entró desde el grupo, el problema es activación/mention gating, no routing.

## Comandos / acciones conceptuales que sirvieron

- crear agente aislado
- inspeccionar bindings
- inspeccionar sesiones activas
- revisar logs del gateway
- editar `openclaw.json` para bindings y `mentionPatterns`
- reiniciar o recargar gateway

## Recomendación operativa

Para futuros agentes de WhatsApp compartido:

- **DM/contacto** → binding por número
- **Grupo** → binding por `group-jid`
- **Grupo con activación por nombre** → añadir `groupChat.mentionPatterns`

## Resultado obtenido

Con este patrón quedó funcionando:
- una sola sesión de WhatsApp
- múltiples agentes aislados
- Ares enroutado al grupo `Smart Project`
- activación por nombre textual `Ares` dentro del grupo

Eso deja una base buena para seguir delegando trabajo a agentes especializados sin abrir más números de WhatsApp.
