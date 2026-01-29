# Proyecto Escuela de Verano
Enfoque para desarrollar la solución a problemática de los carbon brushes en generadores eólicos, desde la perspectiva de una empresa.

## Propiedades del MG1157 Morgan Advanced Materials
Continuous current rating = 18 A/cm2
Continuous speed rating = 40 m/s
Resistivity = 3.30 µΩ·m
Bulk density = 1.30 g/cm³
Metal content = 50% Ag
Common Application = Optimizado para anillos de acero, con capacidad de formar película lubricante estable en climas fríos.

# Solución según profesor:  Equilibrio Termodinámico = Swollen Phase Brush
Traducción:	TDeq favorece la hinchazón del artefacto

## Dato:	La tolerancia (espacio entre pase brush y brush holder) es muy pequeño

# Meta: Proponer un flujo de trabajo para hallar la solución, no la solución en sí misma.
# Restricción: Somos una compañía, no trabajamos como la academia.

# Traducción de propiedades del material

Resistividad: generación localizada de calor, lo que se llama “Joul Heating”
Baja densidad + fase grafito: estructura porosa / capacidad de retención de especies
Contenido metálico 50%: conducción + anclaje mecánico de fases blandas
Optimizado para climas fríos: comportamiento no rígido a bajas temperaturas

# Análisis y presentación del problema
Carbon brushes absorben humedad y sufren hinchazón, se traban mecánicamente, pierden contacto eléctrico y provocan fallas, por lo que deben ser modificados o pueden causar problemas en generadores eólicos

# Posibles causas del problema: Podría ser una o varias
## Contenido metálico del brush
Plata es resistente a la oxidación y con alta conductividad, pero es caro
Debe ser un metal con bajo coeficiente de expansión térmica y alta estabilidad química.

## Contenido carbonoso del brush 
Por qué es grafito
Podria ser otro?
Parece que si o si tiene que ser grafito, pero podría ser otro tipo

## Proporción metal/grafito
¿Bajo qué criterios se establece la proporción ideal?
Quizás la proporción utilizada no es la ideal.

## Porosidad
Análisis porosidad actual -> BET
Análisis de factores que condicionan la porosidad

## Tipo de aglomerante: Resinas Fenolicas
Análisis del tipo de aglomerante utilizado y sus propiedades para determinar si este influye o contribuye a la hinchazón
Estudio de nuevos aglomerantes que contribuyan a disminuir porosidad y/o hinchazón 
Posible combinación de aglomerantes hid

# Posibles soluciones al problema

## Búsqueda de patentes pre existentes
Quizás la solución ya existe, solo que no a nivel comercial 
US4177316A – Impregnated carbon brush for electrical machinery
US3980914A – Brushes for rotating electric machines (Morganite Carbon)
US7067951B2 – Copper-graphite brush
US11764532B2 – Metal graphite grounding brush

## Pre–acondicionamiento del brush
Esto va más conforme a llevar al brush antes de instalarlo a condiciones similares a operación, el brush se expande fuera del generador y se instala ya en su estado de equilibrio.

## Diseño con tolerancia al estado hinchado
Rediseñar housing (brush holder) / resortes de presión, con esto puede llevarse a una aceptación de la expansión como una condición normal, y se puede controlar la presión de contacto.

## Modificación del material para desplazar el equilibrio
Reducir la porosidad efectiva del brush y ajustar su fase metálica (quizás más o menos de carbón o plata) e introducir aditivos hidrofóbicos.
### Aditivos hidrofóbicos 
 Trimetoxisilano (Silanos hidrofóbicos) (pueden dar un tratamiento superficial)
Polidimetilsiloxano (PDMS)
PTFE (Teflon) en micro-particulas (caros, pero pueden extender la vida útil)
Aceites de silicona
### Tener en consideración que no disminuyan la conductividad eléctrica
## Modificaciones del porcentaje de metal:
Reducción ligera del porcentaje metálico (30 – 40%), menor fracción de fases con alto coeficiente de expansión térmica, menor rigidez global del brush, más comportamiento “carbonoso” homogéneo, por lo cual, disminuye le expansión térmica y el estrés interno, sin embargo, podría existir un aumento de resistividad.
Opciones: Bronces especiales como Cu – Sn; Aleaciones de Cu – Ni
## Modificaciones de la síntesis
Composición podría ser la mejor pero no así el método de preparación
## Pruebas que podrían hacerse
Prueba de absorción de humedad
Medición de expansión dimensional
Fricción bajo ambiente controlado
# Tabla

| Aglomerante         | Higroscopicidad | Swelling | Viabilidad industrial |
|---------------------|-----------------|----------|-----------------------|
| Fenólica estándar   | Alta            | Alta     | Muy alta              |
| Fenólica modificada | Media           | Media    | Alta                  |
| Pitch               | Baja            | Baja     | Alta                  |
| Pitch–fenólica      | Muy baja        | Muy baja | Alta                  |
| Furánica            | Muy baja        | Muy baja | Media                 |
| Avanzados           | Mínima          | Mínima   | Baja–Media            |

# Propuesta de solución: cambiar los componentes
## Matriz 4D:
### Carbon compound
(3 tipos de carbono (presentacion de colega de nando)) Es heterogéneo entonces cambiar la proporción de sus componentes
### Aglomerante ()
no sé si es un material homogéneo, de serlo podríamos cambiar entre aglomerantes, si es heterogéneo cambiar la proporcion entre sus componentes.
### Metal
(Cu, Ag, etc)
### Hinchazon final del material

## Pregunta:
Mezclan todo (componentes del carbon compound por separado) o solo los 3?

## To Do:
Analizar cual es el componente/factor/parametro más relevante
luego hacer la matriz de prototipos: ideal no variar los 3 parametros, solo dos:
si fueran 10 condiciones de cada uno, 10*10*10=1000
Quitamos (hipotéticamente) el aglomerante y bajamos a 10*10=100

## Tareas:
Investigar cuales son los componentes de los materiales, tenerlo claro para la presentación.
Identificarnos como departamento de I+D
Reconocer que tenemos recursos ilimitados
Identificar los procesos de cuantificación y los equipos necesarios
Identificar los datos que tenemos
Identificar los datos que faltan y el análisis que debemos proponer
Sugerencia del profe: ponerles precio a los equipos y al proyecto
Mencionar conceptos del curso.