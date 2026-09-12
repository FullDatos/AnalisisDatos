# Sprint Review: análisis exploratorio del dataset Titanic

## 1. Información del sprint

- **Proyecto:** Análisis e Interpretación de Datos.
- **Dataset:** Titanic.
- **Sprint:** Análisis exploratorio y validación inicial.
- **Resultado principal:** Se analizaron 891 registros y siete variables numéricas.

## 2. Objetivo del sprint

Explorar la estructura y el comportamiento inicial del dataset Titanic para identificar patrones, relaciones entre variables, valores extremos y oportunidades de análisis posteriores.

## 3. Trabajo realizado

Durante el sprint se completaron las siguientes actividades:

- Carga y revisión del dataset Titanic.
- Identificación de las variables numéricas disponibles.
- Cálculo de estadísticas descriptivas.
- Elaboración de histogramas para revisar distribuciones.
- Elaboración de un diagrama de caja para identificar valores atípicos.
- Construcción e interpretación de la matriz de correlación.
- Elaboración de un gráfico de dispersión entre `age` y `fare`, segmentado por `pclass`.
- Identificación de variables relevantes para continuar el análisis.

## 4. Resultados obtenidos

- El dataset contiene 891 registros.
- La media de supervivencia es 0.38, equivalente aproximadamente a un 38.4 % de supervivientes.
- La edad promedio es 29.36 años y la mediana es 28 años.
- La tarifa promedio es 32.20, mientras que la mediana es 14.45.
- La tarifa máxima es 512.33 y presenta una distribución sesgada hacia la derecha.
- La mayoría de los pasajeros pertenece a la tercera clase.
- La mayoría de los pasajeros no tenía hermanos, cónyuges, padres o hijos registrados a bordo.

## 5. Hallazgos principales

- La correlación entre `pclass` y `fare` es -0.55. Esto indica que las clases superiores, representadas por valores menores de `pclass`, tienden a asociarse con tarifas más altas.
- La correlación entre `sibsp` y `parch` es 0.41, lo que refleja una relación moderada entre viajar con hermanos o cónyuges y viajar con padres o hijos.
- La correlación entre `survived` y `pclass` es -0.34. Considerando la codificación de las clases, los pasajeros de primera clase presentan una asociación mayor con la supervivencia.
- La correlación entre `survived` y `fare` es 0.26, una relación positiva débil.
- La correlación entre `age` y `fare` es 0.10, por lo que no se observa una relación lineal importante entre edad y tarifa.
- El gráfico de dispersión muestra que las tarifas más altas se concentran principalmente en la primera clase.

## 6. Revisión del incremento

| Historia | Resultado |
|---|---|
| Inspeccionar estructura | Completada para las variables numéricas. |
| Analizar distribuciones | Completada mediante histogramas y estadísticas descriptivas. |
| Analizar correlaciones | Completada mediante matriz de correlación. |
| Revisar valores extremos | Completada inicialmente con diagrama de caja. |
| Analizar relación edad-tarifa | Completada mediante gráfico de dispersión segmentado por clase. |

## 7. Criterios de aceptación revisados

- Las dimensiones y variables numéricas fueron identificadas.
- Se calcularon medidas descriptivas principales.
- Se generaron visualizaciones de distribución.
- Se identificaron valores atípicos en `fare` y otras variables.
- Se calculó la matriz de correlación.
- Se interpretaron las relaciones más relevantes.
- Se generó un gráfico de dispersión funcional con `age`, `fare` y `pclass`.
- Los resultados y limitaciones quedaron documentados.

## 8. Aspectos pendientes

- Analizar las variables categóricas, especialmente `sex` y `embarked`.
- Comparar la supervivencia por sexo y clase.
- Revisar y documentar el tratamiento de valores nulos.
- Confirmar la existencia y el tratamiento de duplicados.
- Crear el dataset procesado en `data/processed/`.
- Evaluar la creación de una variable de tamaño familiar.
- Preparar los datos para PCA mediante codificación y estandarización.


## 9. Demostración para los interesados

Durante la revisión se puede mostrar:

- El resumen estadístico de las variables.
- Los histogramas de `age`, `fare`, `pclass` y `survived`.
- El diagrama de caja para observar valores extremos.
- La matriz de correlación.
- El gráfico de dispersión entre edad y tarifa, diferenciado por clase.
- Las conclusiones sobre la relación entre clase, tarifa y supervivencia.

## 10. Conclusión del sprint

El sprint cumplió su objetivo de establecer una primera comprensión del dataset Titanic. Se identificó que la clase y la tarifa son variables especialmente relevantes para estudiar la supervivencia, mientras que la edad y la tarifa presentan una relación lineal débil. También se detectó la necesidad de tratar los valores atípicos de `fare` con cuidado y de complementar el análisis numérico con variables categóricas antes de obtener conclusiones definitivas.
