# Plantilla de diseño — Encuesta de satisfacción

**Equipo:** 1  
**Integrantes:** Carlos Rojas, David Amanta, Esteban Valenzuela, Ricardo Leon, Alan Tingo   
**Fecha:** 26/10/2026  
**Repositorio (fork):** https://github.com/Rick1751/IDSD422-lab2-diseno-encuesta  
**Enfoque del equipo:** Habitos Alimenticios  

## 1. Objetivo de la encuesta

Evaluar los hábitos alimenticios, patrones de consumo y determinantes psicosociales como el estrés, entorno y alimentación distraída en la población objetivo, con el fin de identificar sesgos perceptivos, conductas automáticas y áreas de oportunidad para la promoción de estilos de vida saludables.

## 2. Población objetivo

- **Población**:Jóvenes de 18 a 25 años trabajadores o estudiantes, que sean habitantes de la zona urbana de Quito, sin importar cuantas veces se alimenten al dia ya sea en su casa o fuera de ella

### Límites del Estudio
**Geográfico:** Exclusivamente la zona urbana de Quito (se excluyen parroquias rurales).  

**Demográfico:** Jóvenes de 18 a 25 años que sean estudiantes o trabajadores.  

**Metodológico:** Sin restricción de frecuencia o lugar de consumo (casa/fuera) para capturar diversidad de conductas.  

**Temporal:** Estudio transversal que analiza el comportamiento actual.  

### Justificación
**Etapa de transición:** Entre los 18 y 25 años se consolidan los hábitos independientes debido al ritmo universitario o laboral.  

**Contexto urbano:** Quito presenta dinámicas de tiempo, movilidad y oferta comercial que condicionan las decisiones de consumo.  

**Identificación de sesgos:** Incluir todo tipo de patrón de ingesta permite contrastar la percepción del participante frente a sus comportamientos reales (estrés, distracción y conveniencia).  
## 3. Método de muestreo

**Método:**
Muestreo no probabilístico por conveniencia. Se seleccionó este método debido a la accesibilidad directa a los participantes y la factibilidad operativa del estudio, lo que permite abordar a las personas en entornos cotidianos y verificar sus criterios de inclusión en el momento.

**Tamaño y justificación:**

La muestra real consta de 15 a 30 participantes. Este tamaño permite obtener un volumen de datos primarios auténticos y manejables dentro del tiempo disponible. Adicionalmente, la base de datos se complementa con registros simulados hasta alcanzar un total de 60 a 100 filas, incluyendo la variable origen (real o simulado) para garantizar la trazabilidad del análisis.

**Cómo se seleccionarán los participantes:**

Los participantes serán contactados de manera virtual e individual a través de canales digitales y redes sociales. Al iniciar la encuesta de google forms, el sistema aplicará preguntas de filtro obligatorias y automatizadas para verificar que la persona cumpla con los criterios de inclusión (tener entre 18 y 25 años, residir en la zona urbana de Quito y ser estudiante o trabajador).

- **Equivalente en código (Python o R):** la línea que implementa tu método sobre un CSV de clientes (aleatorio simple, estratificado o conveniencia) con el resultado de una corrida con semilla, y una frase sobre por qué tu método (y no la conveniencia) justifica el hito.

## 4. Cuestionario (10 preguntas)

*Preguntas neutras, específicas, una idea por pregunta, opciones exhaustivas y excluyentes.*

| #   | Pregunta                      | Tipo de variable              | Dtype al cargar       | Opciones / escala                                                     |
| --- | ----------------------------- | ----------------------------- | --------------------- | --------------------------------------------------------------------- |
| 1   | `edad`                        | Cuantitativa discreta         | `int64`               | Valor numérico (18 a 25)                                              |
| 2   | `ocupacion`                   | Cualitativa nominal           | `category` / `object` | Estudiante, Trabajador, Ambos                                         |
| 3   | `zona_residencia`             | Cualitativa nominal           | `category` / `object` | Urbana Quito (Filtro)                                                 |
| 4   | `lugar_comida_frecuente`      | Cualitativa nominal           | `category` / `object` | Casa, Fuera de casa, Ambos por igual                                  |
| 5   | `frecuencia_ultraprocesados`  | Cualitativa ordinal           | `category`            | 1: Nunca, 2: Rara vez, 3: A veces, 4: Frecuentemente, 5: Casi siempre |
| 6   | `comer_distraido_pantallas`   | Cuantitativa continua / Razón | `float64`             | Porcentaje de comidas frente a pantalla (0.0 a 100.0 %)               |
| 7   | `tiempo_promedio_almuerzo`    | Cuantitativa discreta         | `int64`               | Minutos promedio por comida (ej. 15, 30, 45)                          |
| 8   | `lectura_etiquetas`           | Cualitativa nominal           | `category` / `object` | Ingredientes, Tabla nutricional, Sellos frontales, Ninguna            |
| 9   | `planifica1cion_menu_semanal` | Cualitativa ordinal           | `category`            | 1: Nada planificado, 2: Poco, 3: Moderado, 4: Totalmente planificado  |
| 10  | `influencia_entorno_social`   | Cualitativa ordinal           | `category`            | 1: Sin influencia, 2: Leve, 3: Moderada, 4: Alta influencia           |

### Filtros de elegibilidad y datos generales

**1. Edad**  
`edad`  
¿Cuántos años cumplidos tienes?  
* [ ] Menor de 18 *(Finalizar encuesta)*  
* [ ] 18 a 25 años  
* [ ] Mayor de 25 *(Finalizar encuesta)*  

**2. Ocupación actual**  
`ocupacion`  
¿Cuál es tu ocupación principal?  
* [ ] Estudiante  
* [ ] Trabajador  
* [ ] Ambos (Estudiante y Trabajador)  

**3. Lugar de residencia**  
`zona_residencia`  
¿Resides actualmente en la zona urbana de Quito?  
* [ ] Sí  
* [ ] No 

**4. Lugar de comida frecuente**  
`lugar_comida_frecuente`  
¿Dónde realizas habitualmente la mayoría de tus comidas principales?  
* [ ] En casa  
* [ ] Fuera de casa  
* [ ] Ambos por igual  

**5. Frecuencia de consumo de alimentos ultraprocesados**  
`frecuencia_ultraprocesados`  
¿Con qué frecuencia consumes comida rápida, snacks empaquetados o bebidas azucaradas durante la semana?  
* ( ) 1 - Nunca  
* ( ) 2 - Rara vez  
* ( ) 3 - A veces  
* ( ) 4 - Frecuentemente  
* ( ) 5 - Casi siempre  

**6. Alimentación distraída**  
`comer_distraido_pantallas`  
Aproximadamente, ¿qué porcentaje de tus comidas principales realizas frente a una pantalla (celular, televisión o computadora)?  
*(Ingresa un valor numérico estimado de 0 a 100 %)*  
`[ ________ % ]`  

**7. Tiempo promedio de almuerzo**  
`tiempo_promedio_almuerzo`  
En promedio, ¿cuántos minutos dedicas a tu almuerzo habitual?  
*(Ingresa el tiempo estimado en minutos)*  
`[ ________ minutos ]`  

**8. Lectura de etiquetas nutricionales**  
`lectura_etiquetas`  
Al comprar un producto empaquetado, ¿qué información revisas con mayor frecuencia en la etiqueta?  
* [ ] Ingredientes  
* [ ] Tabla nutricional  
* [ ] Sellos frontales  
* [ ] Ninguna  

**9. Planificación del menú semanal**  
`planificacion_menu_semanal`  
¿En qué medida planificas o preparas con anticipación tu menú semanal de comidas?  
* ( ) 1 - Nada planificado  
* ( ) 2 - Poco  
* ( ) 3 - Moderado  
* ( ) 4 - Totalmente planificado  

**10. Influencia del entorno social**  
`influencia_entorno_social`  
¿En qué grado tus decisiones de alimentación cambian según la compañía (amigos, compañeros de estudio/trabajo o pareja)?  
* ( ) 1 - Sin influencia  
* ( ) 2 - Leve  
* ( ) 3 - Moderada  
* ( ) 4 - Alta influencia


## 5. Análisis de sesgos

*Identifica 2 problemas potenciales de esta encuesta y su mitigación.*

| Sesgo potencial | Mitigación |
| --------------- | ---------- |
| 1.              |            |
| 2.              |            |

## 6. Confidencialidad (RA3)

- Datos personales que se piden y por qué: 
- Plan de anonimización (qué se quita o codifica antes de compartir):

## 7. Verificación con herramientas (Python/R)

*Escribe `scripts/verificacion_encuesta.py` (o `.R`): debe cargar `plantillas/encuesta_respuestas.csv` y reportar los tipos de cada columna, los datos faltantes por columna y la distribución de `satisfaccion_general` y `recomendaria`. Incluye la salida y responde:*

- ¿Coinciden los tipos con tu predicción de la sección 4?
- ¿Cuántos datos faltantes hay por columna?

*Ejecuta el script sobre el CSV final (separa con un filtro de la columna `origen` las filas reales de las simuladas): ¿qué resultado delataría un sesgo de **no respuesta** y cuál un sesgo de **respuesta**? Escribe tu interpretación usando solo las respuestas reales.*
