# Plantilla de diseño — Encuesta de satisfacción (hito 1)

**Equipo:** 1· 
**Integrantes:**Carlos Rojas, David Amanta, Esteban Valenzuela, Ricardo Leon, Alan Tingo   **Fecha:** 26/10/2026
**Repositorio (fork):** https://github.com/Rick1751/IDSD422-lab2-diseno-encuesta
**Enfoque del equipo:** Habitos Alimenticios  

Completa cada sección. Usa commits por sección; la historia del repositorio se revisa.

> **Formato del entregable:** exporta esta plantilla completada a PDF, con el enlace de tu fork en la carátula, y guarda el PDF en `informes/` del fork. Entrega el PDF y el enlace del fork en el aula virtual.

## 1. Objetivo de la encuesta

*Escribe una frase medible: qué decisión de gerencia apoyará esta encuesta.*

## 2. Población objetivo

*Define quién pertenece a la población y justifica los límites (región, edad, frecuencia de compra...). Sugerencia: defínela de modo alcanzable — p. ej., personas 18+ que compran habitualmente en supermercados de tu ciudad — para que tus contactos (familia, amigos) califiquen.*

- Población:
- Límites y justificación:

## 3. Método de muestreo

*Elige aleatorio simple, estratificado o conveniencia y justifica. Meta: 15–30 respuestas reales (3–6 por integrante); opcional: relleno simulado hasta 60–100 filas marcadas con la columna `origen`.*

- Método:
- Tamaño y justificación:
- Cómo se seleccionarán los participantes:
- **Equivalente en código (Python o R):** la línea que implementa tu método sobre un CSV de clientes (aleatorio simple, estratificado o conveniencia) con el resultado de una corrida con semilla, y una frase sobre por qué tu método (y no la conveniencia) justifica el hito.

## 4. Cuestionario (5–10 preguntas)

*Preguntas neutras, específicas, una idea por pregunta, opciones exhaustivas y excluyentes.*

| # | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| ... | | | | |

*Nota: la columna "tipo de variable" usa la clasificación del cap. 3 (numérica continua/discreta, categórica binaria/ordinal). "Dtype al cargar" es cómo crees que llegará la columna en `df.dtypes`/`str()` (`int64`, `float64`, `str`/`object` según la versión de pandas). Pista: el dtype es una pista, no la clasificación — una ordinal puede llegar como `int`.*

## 5. Análisis de sesgos

*Identifica 2 problemas potenciales de esta encuesta y su mitigación.*

| Sesgo potencial | Mitigación |
|---|---|
| 1. | |
| 2. | |

## 6. Confidencialidad (RA3)

- Datos personales que se piden y por qué:
- Plan de anonimización (qué se quita o codifica antes de compartir):

## 7. Verificación con herramientas (Python/R)

*Escribe `scripts/verificacion_encuesta.py` (o `.R`): debe cargar `plantillas/encuesta_respuestas.csv` y reportar los tipos de cada columna, los datos faltantes por columna y la distribución de `satisfaccion_general` y `recomendaria`. Incluye la salida y responde:*

- ¿Coinciden los tipos con tu predicción de la sección 4?
- ¿Cuántos datos faltantes hay por columna?

*Ejecuta el script sobre el CSV final (separa con un filtro de la columna `origen` las filas reales de las simuladas): ¿qué resultado delataría un sesgo de **no respuesta** y cuál un sesgo de **respuesta**? Escribe tu interpretación usando solo las respuestas reales.*
