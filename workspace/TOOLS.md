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

## Notion

- Auth local disponible vía `NOTION_TOKEN`.
- API base: `https://api.notion.com/v1/...`
- Headers típicos en PowerShell:
  - `Authorization: Bearer $env:NOTION_TOKEN`
  - `Notion-Version: 2022-06-28`
- Verificación ya probada: la API respondió bien y el bot autenticado es `Atlas`.
- Página operativa principal: `Atlas OS`.

## Audio / Transcripción

- `ffmpeg` instalado y operativo en esta máquina.
- Versión verificada: `8.1-full_build-www.gyan.dev`.
- Incluye `libwhisper` y soporte amplio de codecs/aceleración.
- Pipeline probado para transcribir audios:
  - `python C:\Users\Gustavo\.openclaw\workspace\scripts\whisper-bridge.py <audio.ogg> --model base --language es`
- Caso real probado: transcribió `Hola Chicichi, vamos.` desde un `.ogg`.

Add whatever helps you do your job. This is your cheat sheet.
