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

Add whatever helps you do your job. This is your cheat sheet.
