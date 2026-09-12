# Informe de análisis exploratorio: dataset Titanic

## 1. Resumen ejecutivo

Se realizó un análisis exploratorio del dataset Titanic con 891 registros y siete variables numéricas: `passengerid`, `survived`, `pclass`, `age`, `sibsp`, `parch` y `fare`.

Los resultados muestran que la supervivencia está relacionada principalmente con la clase del pasajero y, en menor medida, con la tarifa pagada. La correlación entre `survived` y `pclass` fue de -0.34, lo que indica que las personas de clases más altas —representadas por valores menores de `pclass`— tendieron a presentar una mayor supervivencia. La correlación entre `survived` y `fare` fue de 0.26, lo que sugiere una relación positiva débil entre pagar una tarifa más alta y sobrevivir.

La variable `fare` presentó una distribución fuertemente sesgada a la derecha y varios valores extremos. El gráfico de dispersión de `age` frente a `fare`, coloreado por clase, mostró que las tarifas más altas se concentran principalmente en pasajeros de primera clase.

## 2. Objetivo

Analizar las características de los pasajeros del Titanic e identificar patrones asociados con la supervivencia, considerando edad, clase, tarifa pagada y composición familiar.

## 3. Datos analizados

| Variable | Descripción |
|---|---|
| `passengerid` | Identificador del pasajero. |
| `survived` | Supervivencia: 0 = no sobrevivió, 1 = sobrevivió. |
| `pclass` | Clase del pasajero: 1, 2 o 3. |
| `age` | Edad del pasajero. |
| `sibsp` | Hermanos, hermanas, cónyuges o parejas a bordo. |
| `parch` | Padres, madres, hijos o hijas a bordo. |
| `fare` | Tarifa pagada por el pasajero. |

## 4. Estadísticas descriptivas

| Variable | Media | Mediana | Desviación estándar | Mínimo | Máximo |
|---|---:|---:|---:|---:|---:|
| `passengerid` | 446.00 | 446.00 | 257.35 | 1.00 | 891.00 |
| `survived` | 0.38 | 0.00 | 0.49 | 0.00 | 1.00 |
| `pclass` | 2.31 | 3.00 | 0.84 | 1.00 | 3.00 |
| `age` | 29.36 | 28.00 | 13.02 | 0.42 | 80.00 |
| `sibsp` | 0.52 | 0.00 | 1.10 | 0.00 | 8.00 |
| `parch` | 0.38 | 0.00 | 0.81 | 0.00 | 6.00 |
| `fare` | 32.20 | 14.45 | 49.69 | 0.00 | 512.33 |

## 5. Interpretación de las distribuciones

### `passengerid`

La variable presenta una distribución prácticamente uniforme porque funciona como identificador consecutivo. No debe utilizarse como variable explicativa en modelos o interpretaciones de comportamiento.

### `survived`

La media de 0.38 indica que aproximadamente el 38.4 % de los pasajeros sobrevivió y cerca del 61.6 % no sobrevivió. La variable está desbalanceada hacia la categoría 0.

### `pclass`

La tercera clase es la más frecuente, seguida de la primera y la segunda. Esto indica una mayor representación de pasajeros de tercera clase en el dataset.

### `age`

La edad se concentra alrededor de los 28 años. La mayoría de los registros se encuentra aproximadamente entre 20 y 35 años, aunque existen pasajeros desde menos de un año hasta 80 años.

### `sibsp` y `parch`

Ambas variables se concentran en el valor cero. Esto indica que muchos pasajeros viajaban sin hermanos, cónyuges, padres o hijos registrados a bordo. También aparecen algunos valores altos que representan familias más numerosas.

### `fare`

La tarifa presenta una distribución muy sesgada a la derecha. La mediana es 14.45, mientras que la media asciende a 32.20, lo que confirma la influencia de tarifas altas. El valor máximo de 512.33 constituye un valor extremo en comparación con la mayoría de los registros.

## 6. Análisis de correlaciones

| Variables | Correlación | Interpretación |
|---|---:|---|
| `pclass` - `fare` | -0.55 | Relación negativa moderada: las clases con menor número, especialmente la primera, tienden a asociarse con tarifas más altas. |
| `sibsp` - `parch` | 0.41 | Relación positiva moderada: quienes viajaban con hermanos o cónyuges también tendían a viajar con padres o hijos. |
| `pclass` - `age` | -0.34 | Relación negativa débil a moderada: se observa cierta asociación entre clase y edad, aunque no implica causalidad. |
| `survived` - `pclass` | -0.34 | Las clases superiores presentan una mayor asociación con la supervivencia. Como `pclass` usa 1 para primera clase y 3 para tercera, el signo negativo debe interpretarse considerando esa codificación. |
| `survived` - `fare` | 0.26 | Relación positiva débil: las tarifas más altas se asocian parcialmente con una mayor supervivencia. |
| `age` - `sibsp` | -0.23 | Los pasajeros de menor edad tendieron a presentar ligeramente más hermanos o cónyuges registrados. |
| `parch` - `fare` | 0.22 | Relación positiva débil entre viajar con padres o hijos y pagar tarifas mayores. |
| `age` - `fare` | 0.10 | Relación prácticamente débil entre edad y tarifa. |

La correlación no demuestra causalidad. Además, `survived` y `pclass` son variables codificadas numéricamente, por lo que la correlación debe complementarse con comparaciones por grupos.

## 7. Interpretación del gráfico de dispersión

El gráfico representa `age` en el eje horizontal y `fare` en el eje vertical, con colores para las clases 1, 2 y 3.

Se observan los siguientes patrones:

- Los pasajeros de primera clase concentran las tarifas más altas.
- Los pasajeros de tercera clase se agrupan principalmente en tarifas bajas.
- La edad no presenta una relación lineal clara con la tarifa, coherente con la correlación baja de 0.10.
- Existen valores extremos de tarifa cercanos a 500, que deben revisarse, pero no eliminarse automáticamente.
- La clase parece explicar mejor la variación de `fare` que la edad.
- El gráfico presenta concentración de puntos en tarifas bajas, por lo que puede ser útil aplicar una escala logarítmica para visualizar mejor los grupos pequeños y los valores extremos.

## 8. Interpretación del diagrama de caja

El diagrama de caja confirma que `fare` tiene numerosos valores atípicos superiores. También se observan valores extremos en `age`, `sibsp` y `parch`, aunque con menor impacto visual.

El diagrama conjunto no permite comparar directamente la dispersión de todas las variables porque están en escalas diferentes. Para una presentación más precisa, se recomienda generar diagramas separados por variable o agrupar `fare` por `pclass`.

## 9. Conclusiones

1. La supervivencia fue menoritaria: aproximadamente 38.4 % de los pasajeros sobrevivió.
2. La clase del pasajero es una de las variables más relacionadas con la supervivencia.
3. La tarifa pagada tiene una relación positiva débil con la supervivencia y una relación negativa moderada con `pclass`.
4. `fare` es la variable con mayor asimetría y presenta valores atípicos importantes.
5. La edad se concentra alrededor de los 28 años y no tiene una relación fuerte con la tarifa.
6. `sibsp` y `parch` muestran una relación positiva moderada, lo cual es coherente con la presencia de grupos familiares.
7. `passengerid` debe excluirse de análisis predictivos porque solo identifica registros.

## 10. Recomendaciones

- Comparar la tasa de supervivencia por `pclass` y `sex` mediante tablas y gráficos de barras.
- Analizar `fare` por clase utilizando boxplots separados.
- Crear una variable de tamaño familiar, por ejemplo `family_size = sibsp + parch + 1`.
- Evaluar una transformación logarítmica de `fare` debido a su sesgo y valores extremos.
- No eliminar valores atípicos sin verificar si representan pasajeros reales de primera clase.
- Aplicar PCA solo después de excluir identificadores, tratar valores faltantes, codificar categorías y estandarizar las variables.
- Documentar las decisiones de limpieza y mantener el archivo original sin modificaciones.

## 11. Limitaciones

- Las correlaciones muestran asociación lineal y no explican por sí solas la supervivencia.
- `pclass` y `survived` son variables categóricas codificadas como números.
- La información faltante y la transformación de variables pueden modificar los resultados.
- El dataset representa una muestra histórica y no debe generalizarse a otros contextos.

## 12. Resultado de la iteración

El análisis exploratorio permitió conocer la estructura numérica del dataset, identificar patrones de distribución, detectar valores extremos y seleccionar variables relevantes para continuar con el proceso de preparación y análisis.

La siguiente etapa recomendada es completar la evaluación de variables categóricas, documentar el tratamiento definitivo de valores nulos y construir un dataset procesado para análisis avanzado o modelado.
