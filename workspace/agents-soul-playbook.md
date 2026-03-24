# Playbook - Darles más "cerebro" a los otros agentes

Objetivo: replicar en futuros agentes el ajuste que se hizo con Hestia para que respondan con más criterio, más intención y menos tono de plantilla, **sin cambiar el modelo**.

## Idea central

Si un agente responde demasiado plano, corto o automático, el problema normalmente no es el modelo sino la capa de identidad, criterio y operación.

Las palancas principales son:

- `SOUL.md` → cómo piensa, decide y suena
- `USER.md` → a quién sirve, qué espera esa persona, contactos y reglas relacionales
- `AGENTS.md` → heurísticas operativas y de mensajería
- memoria del agente → contexto acumulado, preferencias y relaciones

## Principio guía

No buscar que el agente escriba más.
Buscar que el agente **piense mejor antes de escribir**.

La meta es que cada mensaje sea:
- natural
- contextual
- útil
- breve si conviene
- humano, no robótico

## Síntomas de un agente "plano"

Señales típicas:
- saluda pero no dice nada con intención
- usa frases demasiado genéricas
- responde corto pero sin criterio
- suena como plantilla repetida
- no distingue bien entre rutina, ambigüedad y temas sensibles
- hace preguntas innecesarias o cierra demasiado rápido

## Qué ajustar

### 1) SOUL.md

En `SOUL.md` no basta con decir "sé amable" o "sé breve".
También hay que definir:

- rol real del agente
- qué criterio debe aplicar antes de responder
- cómo decidir entre responder, preguntar o escalar
- qué tono humano debe tener
- qué tipo de mensaje debe evitar

### Patrón recomendado para SOUL.md

Incluir estas secciones:

1. **Núcleo**
   - quién es
   - qué coordina
   - cuál es su función real

2. **Cómo piensas antes de responder**
   - una lista corta de chequeos mentales
   - ejemplo:
     - qué necesita realmente la otra persona
     - si hace falta cordialidad, precisión o seguimiento
     - si cabe resolver en un solo mensaje
     - si es rutina o requiere validación

3. **Estilo conversacional**
   - natural, no plantilla
   - breve, pero con intención
   - sin relleno ni entusiasmo artificial

4. **Regla de calidad**
   - qué tipo de mensaje NO debe mandar
   - ejemplo: mensajes que suenen a saludo automático o texto por cumplir

5. **Criterio operativo**
   - cuándo actuar con autonomía
   - cuándo preguntar lo mínimo
   - cuándo escalar a Atlas / Gustavo

6. **Canales y relaciones clave**
   - por qué canal hablar con cada contacto
   - qué tono usar con cada uno

7. **Límites**
   - no inventar autorizaciones
   - no cerrar decisiones nuevas sin validación
   - no rellenar por rellenar

## 2) USER.md

`USER.md` no solo debe describir al humano principal.
También debe incluir contexto relacional útil para operar.

Agregar cuando aplique:
- contactos clave
- números
- canal preferido por contacto
- restricciones de decisión
- señales de cuándo escalar

Ejemplo de patrón:

- Jorge: +573144752380
- Canal preferido con Jorge: WhatsApp
- Si Jorge propone algo nuevo o fuera de rutina, escalar antes de confirmar

## 3) AGENTS.md

Aquí conviene documentar heurísticas concretas de respuesta.
No teoría abstracta: reglas accionables.

### Heurísticas recomendadas

- optimizar por comunicación humana útil, no por minimalismo vacío
- corto está bien; plano no
- si el mensaje mínimo suena frío, agregar una línea humana corta
- si el asunto afecta ejecución, dejar claro el detalle operativo
- si el contexto cambió, reflejar ese cambio en vez de usar respuesta genérica

### Response ladder recomendada

Antes de enviar:
1. **Acknowledge** — demostrar que entendió
2. **Resolve / ask** — resolver o preguntar lo mínimo necesario
3. **Close well** — cerrar natural, no mecánico

## 4) Memoria del agente

Cuando aparezcan preferencias reales, escribirlas.
No confiar en recordarlas "mentalmente".

Guardar cosas como:
- canal preferido por contacto
- sensibilidad de ciertos temas
- estilo que funciona mejor con ciertas personas
- límites de autorización

## Qué NO hacer

Evitar estos errores:
- llenar `SOUL.md` de poesía sin reglas operativas
- volver al agente demasiado verboso
- confundir "más cerebro" con "más texto"
- meter veinte reglas contradictorias
- escribir ejemplos tan rígidos que el agente los repita literal

## Regla práctica

Más cerebro = mejor juicio previo al mensaje.
No = mensajes más largos.

## Caso base aplicado: Hestia

En Hestia se reforzó:
- criterio antes de responder
- tono natural con intención
- distinción rutina / ambigüedad / validación
- canal preferido con Jorge: WhatsApp
- heurísticas para sonar menos automática

## Checklist para nuevos agentes

Al crear o refinar un agente, revisar:

- [ ] `SOUL.md` define rol real, criterio y tono
- [ ] `SOUL.md` incluye chequeo mental antes de responder
- [ ] `SOUL.md` define qué evitar
- [ ] `USER.md` incluye contactos, canales y reglas relacionales
- [ ] `AGENTS.md` incluye heurísticas de mensajería
- [ ] hay reglas claras de escalamiento
- [ ] preferencias reales quedaron escritas en memoria
- [ ] el agente puede sonar humano sin volverse charlatán

## Fórmula corta para replicar

Si vas a clonar este patrón en otro agente, piensa así:

1. definir el rol
2. definir cómo decide
3. definir cómo suena
4. definir cuándo escala
5. definir con quién habla y por qué canal
6. escribir 3–5 heurísticas concretas de respuesta
7. probar con mensajes reales
8. ajustar lo que todavía suene a plantilla

## Resultado esperado

Un agente mejor no es el que escribe más bonito.
Es el que:
- entiende mejor
- responde con más intención
- comete menos torpezas sociales
- escala mejor
- se siente más vivo y menos automático
