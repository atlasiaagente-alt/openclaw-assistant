# Playbook - Confirmación de handoff entre agentes

Objetivo: evitar falsos positivos cuando Atlas coordina a otro agente y luego reporta que algo ya quedó hecho sin confirmación real en el canal destino.

## Problema a evitar

Una coordinación interna entre agentes no equivale automáticamente a una ejecución real.

Especialmente en canales externos compartidos (como WhatsApp), hay al menos tres niveles distintos:

1. **Orden emitida**
2. **Orden confirmada por el agente responsable**
3. **Acción entregada/visible en el canal externo**

Confundir esos niveles produce errores de operación y reportes falsos de cumplimiento.

---

## Regla operativa

Atlas no debe reportar una tarea como **hecha / resuelta / ejecutada** solo porque:

- envió una instrucción a otro agente
- o recibió una señal interna ambigua
- o asumió que el agente responsable la iba a completar

Para marcar una tarea como verdaderamente ejecutada, debe existir confirmación suficiente.

---

## Estados correctos

### 1) Orden emitida

Usar cuando:
- Atlas ya coordinó al agente responsable
- pero todavía no hay confirmación de ejecución real

Lenguaje recomendado:
- “Coordiné a Ares para ejecutar X.”
- “Orden enviada; pendiente de confirmación.”
- “Se disparó la coordinación, pero aún no confirmo entrega.”

### 2) Orden confirmada

Usar cuando:
- el agente responsable confirma explícitamente que sí ejecutó la acción
- pero Atlas todavía no tiene evidencia clara del canal externo

Lenguaje recomendado:
- “Ares confirmó ejecución.”
- “Pendiente validar entrega visible en el canal.”

### 3) Entrega confirmada en canal externo

Usar solo cuando:
- hay evidencia suficiente de que el mensaje/acción ocurrió realmente en el destino correcto
- por ejemplo, sesión del canal actualizada, mensaje visible o confirmación inequívoca del agente dueño del canal

Solo en este punto Atlas puede reportar:
- “hecho”
- “ejecutado”
- “resuelto”

---

## Regla especial para cron y revisiones de Atlas OS

Cuando un cron de Atlas delega a otro agente, el resumen final debe separar siempre:

- **Órdenes emitidas**
- **Órdenes confirmadas**
- **Entregas confirmadas**

Y debe evitar frases como:
- “ya quedó ejecutado”
- “ya fue resuelto”
- “ya se publicó”

si no existe confirmación real suficiente.

---

## Caso WhatsApp compartido

En WhatsApp compartido, una coordinación correcta no garantiza publicación visible.

Puede fallar por:
- activación
- mention gating
- routing parcial
- interpretación incorrecta del agente
- fallo de entrega
- choque de canal entre Atlas y el agente dueño

Por eso, en estos casos, la carga de prueba para decir “ejecutado” debe ser más alta.

---

## Regla de lenguaje para Atlas

Si no hay confirmación fuerte, Atlas debe hablar con precisión:

- correcto: “lo coordiné”
- correcto: “queda pendiente de confirmación”
- correcto: “no tengo evidencia todavía de que se haya publicado”
- incorrecto: “ya quedó hecho”
- incorrecto: “ya se ejecutó”
- incorrecto: “ya fue enviado”

---

## Incidente base que origina esta regla

Caso: cron de las 7:00 PM de revisión de `Atlas OS`.

Qué pasó:
- el cron sí corrió
- Atlas reportó que Ares ya había ejecutado el recordatorio en `Smart Project`
- luego Ares reconoció que la orden llegó, pero no la convirtió en mensaje visible en el grupo

Lección:
- coordinación interna ≠ ejecución real ≠ entrega confirmada

---

## Regla de mantenimiento

Cuando aparezca un incidente parecido:

1. registrar si hubo orden emitida
2. registrar si hubo confirmación del agente
3. registrar si hubo evidencia de entrega real
4. corregir el lenguaje de los resúmenes futuros
5. actualizar el playbook si aparece un nuevo patrón de fallo
