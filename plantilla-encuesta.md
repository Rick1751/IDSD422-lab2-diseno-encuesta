# Plantilla de diseño — Encuesta de satisfacción

**Equipo:** 1  
**Integrantes:** Carlos Rojas, David Amanta, Esteban Valenzuela, Ricardo Leon, Alan Tingo  
**Fecha:** 08/11/2026  
**Repositorio (fork):** https://github.com/Rick1751/IDSD422-lab2-diseno-encuesta  
**Enfoque del equipo:** Jóvenes de 18 a 25 años que compran en RetailAndina, Quito

## 1. Objetivo de la encuesta

Estimar, dentro de la muestra, la proporción de jóvenes de 18 a 25 años que compran en RetailAndina y califican con 4 o 5 la variedad de alimentos saludables, además de describir su frecuencia de compra. Estos resultados orientarán la decisión de ampliar el surtido saludable y diseñar promociones para ese segmento en Quito.

## 2. Población objetivo

- **Población:** Personas de 18 a 25 años, estudiantes o trabajadoras, residentes en la zona urbana de Quito, que hayan comprado alimentos en RetailAndina al menos una vez en los últimos tres meses.
- **Inclusión:** Cumplir la edad, residir en Quito y tener experiencia reciente de compra en RetailAndina.
- **Exclusión:** Menores de 18 años, mayores de 25, personas que no residan en Quito o que no hayan comprado en RetailAndina en los últimos tres meses.

### Límites del estudio

**Geográfico:** Zona urbana de Quito; se excluyen parroquias rurales y otras ciudades.  
**Demográfico:** Jóvenes de 18 a 25 años que estudian, trabajan o realizan ambas actividades.  
**Comercial:** Compradores recientes de alimentos en RetailAndina, porque pueden evaluar la oferta de la cadena.  
**Temporal:** Percepción y hábitos declarados al momento de responder, durante noviembre de 2026.

### Justificación

El segmento permite estudiar una población alcanzable y relevante para la decisión de surtido y promociones. La experiencia reciente de compra evita pedir opiniones a personas que no conocen RetailAndina, mientras que el límite de Quito mantiene comparable el contexto de tiendas, precios y disponibilidad.

## 3. Método de muestreo

**Método:** Muestreo no probabilístico por conveniencia con referidos declarados. Se contactará a personas accesibles por canales digitales y se verificará la elegibilidad con preguntas filtro. Este método es viable para reunir las 15 a 30 respuestas reales exigidas por la práctica, pero no permite generalizar los resultados a todos los jóvenes de Quito; esa limitación se declarará en el informe.

**Tamaño y justificación:** Se recolectaron 24 respuestas reales, dentro de la meta de 15 a 30 respuestas exigida por la práctica. Para practicar el análisis sin confundirlas con evidencia de campo, se generaron 100 registros simulados con código, marcados en `origen`; nunca se presentan como respuestas reales.

**Cómo se seleccionarán los participantes:** Cada integrante difundirá el formulario a contactos de 18 a 25 años que vivan en Quito y hayan comprado en RetailAndina en los últimos tres meses. El formulario finalizará para quienes no cumplan los filtros. Se procurará diversidad de edades, ocupación y frecuencia de compra.

**Equivalente en Python (selección por conveniencia):**

```python
import pandas as pd

respuestas = pd.read_csv("plantillas/encuesta_respuestas.csv")
elegibles = respuestas.query(
    "origen == 'real' and edad >= 18 and edad <= 25 "
    "and compra_reciente_retailandina == 'Sí'"
)
muestra = elegibles.sample(
    n=min(30, len(elegibles)),
    random_state=422,
)
print(muestra[["respuesta_id", "edad", "ocupacion"]])
```

El formulario verificó la residencia en Quito, pero esa variable no se guarda en el CSV para minimizar datos personales. `sample()` selecciona de forma reproducible hasta 30 casos elegibles disponibles; no constituye un muestreo aleatorio de toda la ciudad. Por ello los resultados se interpretarán como descriptivos de la muestra.

## 4. Cuestionario (10 preguntas)

Las preguntas son neutras, específicas y corresponden a una sola idea. Las preguntas 1 y 3 funcionan como filtros de elegibilidad.

| # | Variable | Pregunta | Tipo de variable | Dtype al cargar | Opciones / escala |
|---|---|---|---|---|---|
| 1 | `edad` | ¿Cuántos años cumplidos tienes? | Cuantitativa discreta | `int64` | Valor numérico de 18 a 25 |
| 2 | `ocupacion` | ¿Cuál es tu ocupación actual? | Cualitativa nominal | `object` | Estudiante, Trabajador, Ambos |
| 3 | `compra_reciente_retailandina` | ¿Has comprado alimentos en RetailAndina durante los últimos tres meses? | Cualitativa nominal | `object` | Sí, No |
| 4 | `frecuencia_compra_retailandina` | ¿Con qué frecuencia compras alimentos en RetailAndina? | Cualitativa ordinal | `object` | Varias veces por semana, Semanal, Quincenal, Mensual, Menos de una vez al mes |
| 5 | `frecuencia_ultraprocesados` | ¿Con qué frecuencia consumes alimentos ultraprocesados, es decir, comida rápida, snacks empaquetados y bebidas azucaradas en conjunto? | Cualitativa ordinal | `int64` | 1 Nunca, 2 Rara vez, 3 A veces, 4 Frecuentemente, 5 Casi siempre |
| 6 | `comer_distraido_pantallas` | De los alimentos que compras en RetailAndina, ¿qué porcentaje aproximado de tus comidas principales realizas frente a una pantalla? | Cuantitativa continua | `float64` | Número de 0 a 100 |
| 7 | `tiempo_promedio_almuerzo` | En promedio, ¿cuántos minutos dedicas a tu almuerzo habitual preparado con alimentos comprados en RetailAndina? | Cuantitativa discreta | `int64` | Número entero en minutos |
| 8 | `lectura_etiquetas` | ¿Qué información revisas en la etiqueta de un producto empaquetado? Puedes marcar más de una. | Cualitativa nominal múltiple | `object` | Ingredientes, Tabla nutricional, Sellos frontales, Ninguna |
| 9 | `planificacion_menu_semanal` | ¿En qué medida planificas o preparas con anticipación tu menú semanal? | Cualitativa ordinal | `int64` | 1 Nada, 2 Poco, 3 Moderado, 4 Totalmente |
| 10 | `satisfaccion_variedad_saludable` | ¿Qué tan satisfecho o satisfecha estás con la variedad de alimentos saludables en RetailAndina? | Cualitativa ordinal | `int64` | 1 Muy insatisfecho/a, 2 Insatisfecho/a, 3 Ni satisfecho/a ni insatisfecho/a, 4 Satisfecho/a, 5 Muy satisfecho/a |

### Formulario

**1. Edad — `edad`**  
¿Cuántos años cumplidos tienes? Respuesta numérica. Si está fuera de 18 a 25, finalizar la encuesta.

**2. Ocupación — `ocupacion`**  
¿Cuál es tu ocupación actual?

- Estudiante
- Trabajador
- Ambos (estudiante y trabajador)

**3. Compra reciente — `compra_reciente_retailandina`**  
¿Has comprado alimentos en RetailAndina durante los últimos tres meses?

- Sí
- No (finalizar la encuesta)

**4. Frecuencia de compra — `frecuencia_compra_retailandina`**  
¿Con qué frecuencia compras alimentos en RetailAndina?

- Varias veces por semana
- Semanal
- Quincenal
- Mensual
- Menos de una vez al mes

**5. Consumo de ultraprocesados — `frecuencia_ultraprocesados`**  
¿Con qué frecuencia consumes alimentos ultraprocesados, es decir, comida rápida, snacks empaquetados y bebidas azucaradas en conjunto?

- 1 — Nunca
- 2 — Rara vez
- 3 — A veces
- 4 — Frecuentemente
- 5 — Casi siempre

**6. Alimentación frente a pantallas — `comer_distraido_pantallas`**  
De los alimentos que compras en RetailAndina, ¿qué porcentaje aproximado de tus comidas principales realizas frente a una pantalla (celular, televisión o computadora)? Ingresa un número de 0 a 100.

**7. Tiempo de almuerzo — `tiempo_promedio_almuerzo`**  
En promedio, ¿cuántos minutos dedicas a tu almuerzo habitual preparado con alimentos comprados en RetailAndina? Ingresa un número entero.

**8. Lectura de etiquetas — `lectura_etiquetas`**  
¿Qué información revisas en la etiqueta de un producto empaquetado? Puedes marcar más de una.

- Ingredientes
- Tabla nutricional
- Sellos frontales
- Ninguna

**9. Planificación del menú — `planificacion_menu_semanal`**  
¿En qué medida planificas o preparas con anticipación tu menú semanal?

- 1 — Nada
- 2 — Poco
- 3 — Moderado
- 4 — Totalmente

**10. Variedad saludable en RetailAndina — `satisfaccion_variedad_saludable`**  
¿Qué tan satisfecho o satisfecha estás con la variedad de alimentos saludables en RetailAndina?

- 1 — Muy insatisfecho/a
- 2 — Insatisfecho/a
- 3 — Ni satisfecho/a ni insatisfecho/a
- 4 — Satisfecho/a
- 5 — Muy satisfecho/a

## 5. Análisis de sesgos

| Sesgo potencial | Cómo podría aparecer | Mitigación |
|---|---|---|
| Sesgo de selección | La muestra se obtiene de contactos de los integrantes y puede sobre representar estudiantes, conocidos y clientes frecuentes. | Usar referidos de perfiles distintos, buscar variedad de edades y ocupación, aplicar los mismos filtros a todos y declarar que el muestreo es por conveniencia. |
| Sesgo de respuesta | Una persona puede declarar mayor satisfacción por cortesía o evitar criticar a RetailAndina. | Aplicar una encuesta anónima, no pedir nombre ni correo, usar redacción neutral, permitir respuestas intermedias y explicar que no afecta sus compras ni beneficios. |

## 6. Confidencialidad (RA3)

- **Datos personales que se piden y por qué:** edad, ocupación y zona urbana de residencia se solicitan únicamente para comprobar la población objetivo y describir la muestra. También se registra la frecuencia de compra, que es un dato de comportamiento necesario para el objetivo. No se piden nombres, cédulas, teléfonos, correos, direcciones exactas ni datos financieros.
- **Plan de anonimización:** cada respuesta recibe un código como `R001`; no se almacenan identificadores directos ni coordenadas. Antes de compartir el CSV se eliminan campos accidentales que puedan identificar a una persona, se conserva solo la zona urbana de Quito y se separan los registros simulados mediante `origen`. El archivo crudo del formulario no se publica en el repositorio y el CSV compartido contiene únicamente datos anonimizados.

## 7. Verificación con herramientas (Python/R)

Se ejecuta `python scripts/generar_datos_simulados.py` para generar las 100 filas simuladas y luego `python scripts/verificacion_encuesta.py` desde la raíz. El script de verificación carga `plantillas/encuesta_respuestas.csv`, que contiene las respuestas reales y simuladas, imprime los tipos, los datos faltantes y las distribuciones de las variables principales (`frecuencia_compra_retailandina` y `satisfaccion_variedad_saludable`), separando además las respuestas reales de las simuladas.

El CSV final contiene 124 respuestas: 24 marcadas como `real` y 100 como `simulada`. Las filas simuladas también se conservan por separado en `plantillas/encuesta_simulada.csv` para dejar reproducible su generación; no se presentan como evidencia de recolección real.
La salida completa de la auditoría se conserva en `informes/verificacion.txt`.

**No respuesta:** se invitó a 30 personas y se obtuvieron 24 respuestas reales completas. Por tanto, se registraron 6 no respuestas y una tasa de no respuesta de 20.0%. Las 100 filas simuladas no se incluyen en este cálculo.

**Interpretación de la auditoría:**

- En las 24 respuestas reales, el 66.7% calificó con 4 o 5 la variedad saludable; la media fue 3.83 y no hubo calificaciones de 1. La satisfacción es alta y esto podría indicar sesgo de respuesta por cortesía, pero con n=24 y muestreo por conveniencia no se puede confirmar.
- `compra_reciente_retailandina` es «Sí» en todas las 24 filas reales porque quienes respondían «No» terminaban la encuesta (filtro de elegibilidad), por lo que esta variable no aporta variación.
- De la no respuesta (6 de 30, 20.0%) no se registró información de quienes no respondieron, así que no se puede comprobar si se concentra en algún subgrupo; es una limitación, no una conclusión.
- Las filas simuladas no se usan para interpretar sesgos; la interpretación es descriptiva de la muestra real y no es generalizable a toda la población.
