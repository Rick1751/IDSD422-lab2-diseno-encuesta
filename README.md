# Laboratorio 2: Diseño de una encuesta de satisfacción

**Caso empresarial:** RetailAndina S.A., cadena ecuatoriana de tiendas de consumo masivo.

**Sesión de trabajo:** martes 20 de octubre de 2026 (18:00–20:00, en equipos del proyecto) · **Entrega del borrador:** al final de esa sesión · **Hito 1 final (con datos):** martes 10 de noviembre.

## El contexto

RetailAndina va a lanzar un programa de fidelización y la gerencia quiere saber qué tan satisfechos están sus clientes y qué esperan del programa. Tu equipo de Business Intelligence tiene que diseñar la encuesta que medirá esa satisfacción: decidir a quién preguntar (población y muestra), cómo seleccionar a esas personas (método de muestreo) y qué preguntar (cuestionario), anticipando los problemas típicos de las encuestas.

**Tu rol:** analista del equipo de BI. Completas la plantilla de diseño con tu equipo y la presentas como **borrador del hito 1 del proyecto**. Después, en la semana del feriado (2 y 3 de noviembre no hay clases) aplicas la encuesta a una muestra real pequeña y, si quieres más datos, la completas con valores simulados declarados. El hito final se entrega el martes 10 de noviembre.

## Enfoque del equipo (Opción B)

Todos los equipos diseñan sobre **RetailAndina**, pero cada equipo elige un **enfoque o segmento distinto**; el docente lo aprueba en clase y **no puede haber dos equipos con el mismo enfoque**. El mismo diseño es el **Hito 1** del proyecto: el lab 2 califica el borrador (20/10) y el Hito 1 el final con datos (10/11).

**Ejemplos de enfoques** (elige uno y escríbelo en la cabecera de la plantilla):

- Programa de fidelización: satisfacción y beneficios valorados.
- Precios: percepción frente a la competencia.
- Atención en caja: rapidez y amabilidad.
- Variedad y stock: satisfacción y disponibilidad.
- Compra en línea / app: experiencia.
- Limpieza y comodidad: ambiente de la tienda.
- Jóvenes (18–29): satisfacción y expectativas.
- Familias: hábitos de compra semanal.
- Frecuentes vs. ocasionales: satisfacción y lealtad.
- Por ciudad: Quito, Guayaquil y Cuenca.

Si hay más equipos que enfoques, combina un enfoque con un segmento (por ejemplo, "precios en clientes jóvenes").

## Objetivos de la práctica

**Objetivo general:** diseñar la encuesta de satisfacción del programa de fidelización de RetailAndina, lista para aplicarse: objetivo medible, población y muestra alcanzables, método de muestreo justificado, cuestionario de 5 a 10 preguntas y plan de manejo de sesgos y confidencialidad, con la verificación de los datos implementada en Python o R.

**Al terminar la práctica podrás:**

1. **Formular** un objetivo de encuesta medible, ligado a una decisión concreta de la gerencia.
2. **Definir** la población objetivo y **justificar sus límites** (quién entra, quién no y por qué).
3. **Elegir y justificar** un método de muestreo (aleatorio simple, estratificado o conveniencia declarada) e **implementarlo en código**.
4. **Redactar** un cuestionario de 5 a 10 preguntas neutras, específicas y de una sola idea, y **clasificar** cada una por tipo de variable y dtype esperado al cargarla.
5. **Anticipar** los sesgos típicos de una encuesta (selección, no respuesta y respuesta) con **mitigaciones viables**, y aplicar las reglas de confidencialidad (RA3).
6. **Auditar** el CSV de respuestas con un script (tipos, datos faltantes y distribuciones) e **interpretar** qué patrón delataría cada sesgo.

Cada objetivo tiene su sección en la plantilla y su criterio en `EVALUACION.md`: objetivo (1), población (2), muestreo (3), cuestionario (4), sesgos (5), confidencialidad (6) y verificación (7).

## Archivos del repositorio

- `README.md`: este documento, con el contexto del caso y los objetivos
- `plantilla-encuesta.md`: el entregable: la plantilla de diseño que completas sección por sección
- `plantillas/encuesta_respuestas.csv`: plantilla para registrar las respuestas, una fila por persona
- `plantillas/encuesta_simulada.csv`: 100 respuestas simuladas reproducibles
- `scripts/generar_datos_simulados.py`: generador de respuestas simuladas
- `scripts/verificacion_encuesta.py`: script de auditoría de las respuestas
- `informes/verificacion.txt`: salida de la auditoría ejecutada
- `EVALUACION.md`: la rúbrica con la que se evalúa el laboratorio

## Requisitos

- **Python 3.9 o superior** con `pandas` (`pip install pandas`), **o R 4.x** (el script de verificación se resuelve con R base; si tu muestreo usa dplyr, instala `tidyverse`).
- Sin instalación: Google Colab (Python) o Posit Cloud (R), donde hicimos la Práctica 1.
- Para el borrador **no** se recolectan datos: eso ocurre en la semana del feriado.

## El componente de código (Python o R, tú eliges)

El diseño se completa con código en tres momentos:

1. **Muestreo en código (sección 3).** La línea que implementa el método de muestreo que elegiste, probada sobre un CSV de clientes. Piensa en las funciones de selección aleatoria que viste en clase.
2. **Dtype esperado (sección 4).** Anota cómo crees que llegará cada columna del cuestionario al cargar el archivo. Recuerda el cap. 3: el dtype es una pista, no la clasificación.
3. **Verificación de sesgos (sección 7).** Escribes un script que audite el CSV de respuestas (tipos, datos faltantes y distribuciones). Lo corres primero sobre la plantilla y luego sobre tus datos reales, y lo interpretas.

**Cómo ejecutar el script** desde la raíz del repositorio:

```bash
python scripts/generar_datos_simulados.py
python scripts/verificacion_encuesta.py
```

## Cómo trabajar y entregar

1. Haz un **fork** de este repositorio: tu fork es tu entrega.
2. Trabaja sobre tu copia (clónala en Posit Cloud o con `git clone`) y completa la plantilla sección por sección: objetivo, población, muestreo, cuestionario, sesgos, confidencialidad y verificación con código.
3. Haz un **commit por cada sección completada**, con mensajes claros; la historia del repositorio se revisa.
4. Pilotea el cuestionario con dos compañeros (hay bonus) y ajusta lo que haga falta.
5. En la semana del feriado aplica la encuesta y registra las respuestas (ver abajo).
6. **Entrega el PDF de la plantilla completada y el enlace de tu fork**: exporta `plantilla-encuesta.md` a PDF con el enlace del fork en la carátula y guarda el PDF en `informes/` del fork. Borrador: al final de la sesión del martes 20/10; hito final con datos: martes 10/11.

## Recolección de datos (semana del feriado)

Tu meta es conseguir entre 15 y 30 respuestas reales por equipo, unas 3 a 6 por integrante. La vía más práctica: envía el formulario (o la encuesta en papel) a familiares, amigos y compañeros que califiquen en tu población, por WhatsApp, correo o en persona. Para practicar los análisis del capítulo 4 y del laboratorio 7, este repositorio incluye 100 filas simuladas generadas con código, marcadas en la columna `origen` como simulada. Eso se declara en el informe: simular no es inventar en silencio.

Las filas del CSV de plantilla son solo ejemplos de formato (incluida una simulada). Se reemplazan con tus datos y ajustas las columnas a tu cuestionario (una columna por pregunta, más la columna `origen`).

1. **Población (sección 2).** Defínela de modo que sea alcanzable. Una opción práctica: personas de 18 años o más que compran habitualmente (al menos una vez al mes) en supermercados de su ciudad. Así tus contactos califican, y el canal (familiares y amigos) se declara como muestreo por conveniencia más referidos, mitigando los sesgos que identificaste en la sección 5.
2. **Instrumento.** Monta el cuestionario aprobado en el borrador, con las mismas preguntas y opciones de la sección 4. Si aplicas opciones distintas, el CSV termina con categorías inconsistentes, por ejemplo "a veces" contra "aveces".
3. **Aplicación real.** Registra una fila por persona con `origen = real`, código de respuesta (R001...), fecha en formato ISO y las opciones exactas del cuestionario.
4. **Relleno simulado (opcional).** `scripts/generar_datos_simulados.py` genera 100 filas con semilla `422`, respetando las opciones del cuestionario y distribuciones plausibles. Las filas quedan en `plantillas/encuesta_simulada.csv` y también se incorporan al CSV final con `origen = simulada`.
5. **Anonimización (RA3).** No pongas nombres ni correos. El archivo crudo no se sube al repositorio.
6. **Auditoría.** Ejecuta el script de verificación sobre el CSV final y separa las filas reales de las simuladas (filtra la columna `origen`) para que la interpretación de sesgos use solo datos reales.
7. **No respuesta.** Registra las invitaciones, respuestas completas y no respuestas. En este proyecto se invitaron 30 personas, se obtuvieron 24 respuestas reales completas y se registraron 6 no respuestas (20.0%).

## Entregables

- **Borrador (práctica, martes 20 de octubre, al final de la sesión).** `plantilla-encuesta.md` completa, con los tres componentes de código escritos, y el **PDF en `informes/`** del fork.
- **Hito 1 final (martes 10 de noviembre).** Plantilla refinada, CSV anonimizado con 24 respuestas reales y 100 simuladas marcadas en la columna `origen`, la salida interpretada del script de verificación y el **PDF actualizado en `informes/`**; entrega el PDF + el enlace del fork.

La evaluación está detallada en `EVALUACION.md` (rúbrica de 100 puntos; la nota es puntos ÷ 100 × 20).

*Laboratorio 2, IDSD422, Estadística y Programación para Ciencia de Datos I, 2026-B.*
