Basado en el documento PDF que compartiste, tus compañeros están abordando un problema técnico específico con una pieza llamada **Carbon Brush MG1157** y han diseñado una metodología experimental para solucionarlo.

Aquí tienes el desglose de lo que están haciendo:

### 1. El Problema que Intentan Resolver

Están investigando una falla por **"Hinchamiento Interno" (Internal Swelling)** en las escobillas.

* La pieza actual (MG1157) es una escobilla de metal-grafito (50%).


* Esta pieza tiene una **tolerancia mecánica muy reducida** con su soporte.


* El problema es que el material se hincha, aumenta su porosidad y probablemente se atasca o falla, debido a un desequilibrio "termo-electro-mecánico".



### 2. Diagnóstico de la Causa Raíz

Han identificado que el problema nace en el proceso de fabricación, específicamente en cómo interactúan los materiales durante las etapas de **Conformado** y **Carbonización**.

* Identificaron que el **aglomerante (binder)** es un componente crítico responsable de la hinchazón y la relajación térmica.


* Señalaron que la porosidad interna se genera cuando el binder se descompone durante la carbonización ().



### 3. La Propuesta Experimental (Lo que van a hacer ahora)

El equipo ha diseñado un **Plan de Diseño de Experimentos (DOE)** para encontrar una nueva fórmula o proceso de fabricación que elimine el hinchamiento. Su plan consta de 4 fases:

* **Fase 1: Definición de Variables Críticas**
Van a modificar 4 parámetros clave respecto al proceso actual:


1. 
**Tipo de Aglomerante:** Probarán nuevos binders en lugar del orgánico actual.


2. 
**Presión de Prensado:** Experimentarán con nuevas presiones.


3. 
**Temperatura de Carbonización:** Ajustarán los rangos de temperatura.


4. 
**Recubrimiento/Impregnación:** Buscarán alternativas al "Carbon black" actual.




* **Fase 2: Análisis de Sensibilidad**
Utilizarán análisis estadístico (**ANOVA**) para entender qué variables afectan más a la densidad del material (*Bulk density*).


* 
**Herramienta:** Están utilizando **Jupyter** (Python) para procesar estos datos.




* **Fase 3: Diseño Factorial**
Ejecutarán un diseño experimental factorial para cruzar estas variables y ver cómo interactúan entre sí.


* **Fase 4: Selección Final (Pareto)**
Usarán un diagrama de **Pareto** (también procesado en Jupyter) para identificar los parámetros que tienen el mayor impacto positivo y seleccionar la formulación final óptima.



### Resumen

En términos sencillos: Tus compañeros han detectado que la "receta" actual de las escobillas hace que se hinchen. Van a "cocinar" varios lotes de prueba cambiando ingredientes (binder), temperatura y presión, y usarán análisis de datos en Python (Jupyter) para determinar científicamente cuál es la combinación perfecta que evita el problema.

¿Te gustaría que profundice en la parte del análisis estadístico con Jupyter que mencionan en el PPT?