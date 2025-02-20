# Caracterización de Enfermedades mediante MIMIC-IV

Este repositorio contiene el código del Trabajo de Fin de Máster (TFM) titulado **"Caracterización de enfermedades de origen orgánico mediante parámetros clínicos aplicando métodos de ensamble y minería de reglas"**. El objetivo del proyecto es explorar la relación entre parámetros bioquímicos y diagnósticos mediante minería de reglas de asociación y clasificación con modelos de ensamble, utilizando el conjunto de datos MIMIC-IV.

## Tabla de Contenidos

- [Introducción](#introducción)
- [Objetivos](#objetivos)
- [Metodología](#metodología)
- [Conclusiones](#conclusiones)
- [Licencia](#licencia)
- [Autor](#autor)

---

## Introducción

El diagnóstico de enfermedades relacionadas con disfunciones orgánicas es un desafío debido a la heterogeneidad de los datos clínicos. Tradicionalmente, los métodos basados en umbrales individuales pueden pasar por alto interacciones complejas entre parámetros. Este proyecto combina **minería de reglas de asociación** y **modelos de ensamble** para descubrir patrones clínicos ocultos y mejorar la precisión diagnóstica.

## Objetivos

### Objetivo Principal
Desarrollar un modelo de aprendizaje supervisado basado en minería de reglas y técnicas de ensamble para la **caracterización de enfermedades** en pacientes hospitalizados en la base de datos **MIMIC-IV**.

### Objetivos Secundarios
- Analizar y preprocesar MIMIC-IV con herramientas de Big Data.
- Implementar **algoritmos de minería de reglas** (FP-Growth, Apriori) para detectar relaciones clínicas.
- Entrenar modelos predictivos basados en **XGBoost** para la predicción de diagnósticos.
- Diseñar una **interfaz interactiva** para la consulta de predicciones.

## Metodología

1. **Extracción y preprocesamiento** de datos desde MIMIC-IV usando **Google BigQuery** y **Apache Spark**.
2. **Transformación de datos** en un formato transaccional para minería de reglas.
3. **Generación de reglas de asociación** utilizando el algoritmo **FP-Growth**.
4. **Entrenamiento de modelos de ensamble** para la predicción de diagnósticos.
5. **Interpretación de modelos** con valores **SHAP** para explicar la contribución de cada variable en las predicciones.
6. **Desarrollo de una interfaz en Gradio** para la visualización interactiva de resultados.

## Conclusiones

El presente trabajo muestra el valor de la combinación de la **minería de reglas de asociación** y los **modelos de clasificación supervisados** en la caracterización de patrones clínicos y la predicción de diagnósticos en grandes volúmenes de datos sanitarios.

Se ha observado que algunos modelos alcanzan un rendimiento destacado, logrando **métricas de ROC-AUC superiores a 0.94**, lo que indica una alta capacidad discriminativa en la clasificación de enfermedades. Sin embargo, también se identificaron desafíos, como el manejo del **desbalance de clases**, que afectó la predicción en algunos diagnósticos con menor representación.

El uso de **valores SHAP** ha permitido mejorar la explicabilidad del modelo, proporcionando información clara sobre la contribución de cada variable en las predicciones. Esto es crucial en entornos clínicos, donde la interpretabilidad del modelo es tan importante como su precisión.

Entre las limitaciones del estudio, destaca la necesidad de evaluar estrategias más avanzadas para el **manejo del desbalanceo de clases**, así como explorar enfoques adicionales para mejorar la **generalización del modelo** a distintos subgrupos poblacionales. Además, futuras investigaciones podrían integrar más datos clínicos y aplicar técnicas de modelado probabilístico para optimizar la precisión del diagnóstico.

En conclusión, este trabajo demuestra que la inteligencia artificial y el big data pueden desempeñar un papel clave en la medicina, permitiendo extraer conocimiento útil a partir de grandes volúmenes de datos clínicos y contribuyendo a la toma de decisiones médicas más informadas.

## Licencia

Este proyecto utiliza datos de la base de datos **MIMIC-IV**, los cuales son propiedad de **PhysioNet** y están sujetos a restricciones de acceso. Para acceder a estos datos, es necesario solicitar autorización a través de [PhysioNet](https://physionet.org/content/mimiciv/) y completar el proceso de certificación requerido. El uso de los datos debe cumplir con las normativas de protección de datos y ética establecidas por PhysioNet.

El código de este repositorio se distribuye bajo la licencia **MIT**, permitiendo su libre uso, modificación y distribución bajo los términos especificados en el archivo `LICENSE`.

## Autor

Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
- Nombre: Nuria Mansilla
- Email: nuria.mansilla.fernandez@gmail.com
- LinkedIn: https://www.linkedin.com/in/numansilla/
