# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## WhatsApp

### Native polls in WhatsApp groups via OpenClaw CLI

Ares verified that native WhatsApp polls can be sent from this setup with `openclaw message poll`.

Example for the `Smart project` group:

```powershell
openclaw message poll --target 120363424964463765@g.us --poll-question "Prueba de encuesta Ares" --poll-option "Sí" --poll-option "No" --poll-option "Probando"
```

Reusable pattern:

```powershell
openclaw message poll --target <group-id@g.us> --poll-question "<pregunta>" --poll-option "<opcion 1>" --poll-option "<opcion 2>"
```

Notes:
- WhatsApp supports 2-12 options in this flow.
- Add `--poll-multi` if you want multi-select.
- This sends the native WhatsApp poll UI, not a text imitation.
- Verified working in `Smart project` on 2026-03-25.

## Smart Project - Diccionario vivo

### Palabras y usos aprendidos
- **parce**: base natural del tono del grupo.
- **de una** / **sí de una**: acuerdo, validación, cierre natural.
- **paila / pailas**: algo no salió, tocó ajustar o se cayó la idea.
- **qué fue**: saludo corto o entrada casual.
- **bacano**: algo salió bien o se siente bueno.
- **meterle / darle**: ejecutar, arrancar, cumplir.
- **vaina / cosa**: comodín, pero no abusar en mensajes donde Gustavo ya marcó que suena flojo.
- **tris**: un momento corto.
- **fino**: algo quedó limpio, bien dicho o bien armado.
- **marica / maricas**: cercanía o peso emocional; usar solo cuando salga natural en contexto humano.
- **mariquita**: pulla o reclamo suave cuando alguien se está echando para atrás; usar con mucha medida.
- **sapo**: meterse donde no llamaron o comentar de más.

### Reglas de tono para Smart Project
- No usar **criterio** al hablar con el grupo; Gustavo pidió sacarla del vocabulario.
- Si ya hubo check-in y el estado quedó claro, no repetir seguimiento.
- No soltar backstage: nada de logs, "mensaje enviado", message ids ni reportes internos.
- Si la conversa es puro lore humano y no hace falta ayuda real, mejor quedarse sano.
- Aprender jergas del grupo, pero no meterlas por relleno ni sonar forzado.

Add whatever helps you do your job. This is your cheat sheet.
