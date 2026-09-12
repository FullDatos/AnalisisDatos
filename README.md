# Análisis e Interpretación de Datos: Titanic

## Descripción del proyecto

Este proyecto desarrolla un proceso de preparación, validación y análisis exploratorio de datos usando el dataset **Titanic**. El objetivo es aplicar buenas prácticas de organización, calidad, limpieza, análisis descriptivo e interpretación de datos.

El trabajo se organiza mediante historias de usuario relacionadas con la identificación de fuentes, incorporación y conservación del dataset original, inspección de estructura, tratamiento de valores faltantes y duplicados, normalización de formatos, análisis de distribuciones, correlaciones y reducción de dimensionalidad mediante PCA.

## Objetivo general

Analizar las características de los pasajeros del Titanic e identificar patrones asociados con la supervivencia, considerando variables como clase del boleto, sexo, edad, tarifa pagada, familiares a bordo y puerto de embarque.

## Pregunta de análisis

> ¿Qué características de los pasajeros, tales como sexo, clase, edad y tarifa, se relacionan con la probabilidad de supervivencia en el Titanic?

## Dataset seleccionado

- **Nombre:** Titanic - Machine Learning from Disaster
- **Tema:** Información de pasajeros del Titanic y su condición de supervivencia.
- **Formato esperado:** CSV.
- **Archivo principal recomendado:** `train.csv`.
- **Ubicación del archivo original en el proyecto:** `data/raw/dataset.csv`.
- **Fuente sugerida:** [Kaggle: Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data).

El archivo original se conservará sin modificaciones en la carpeta `data/raw/`. Cualquier dataset transformado, limpio o preparado para análisis deberá guardarse en una carpeta diferente, como `data/processed/`.

## Estructura del proyecto

```text
.
├── .github/
│   └── workflows/              # Flujos de automatización o CI/CD
├── data/
│   ├── raw/                    # Dataset original, sin modificaciones
│   │   └── dataset.csv
│   └── processed/              # Datasets limpios o transformados
├── notebooks/                  # Análisis exploratorio y pruebas
├── src/                        # Código reutilizable del proyecto
├── tests/                      # Pruebas de validación de datos o código
├── README.md
└── requirements.txt
```

## Diccionario de datos

| Variable | Tipo de dato | Descripción |
|---|---|---|
| `PassengerId` | Entero | Identificador único de cada pasajero. |
| `Survived` | Entero / categórica | Indica si el pasajero sobrevivió: `0` = no sobrevivió, `1` = sobrevivió. |
| `Pclass` | Entero / categórica | Clase socioeconómica del boleto: `1` = primera, `2` = segunda, `3` = tercera. |
| `Name` | Texto | Nombre completo del pasajero. |
| `Sex` | Categórica | Sexo registrado del pasajero. |
| `Age` | Decimal | Edad del pasajero en años. Puede contener valores faltantes. |
| `SibSp` | Entero | Número de hermanos, hermanas, cónyuges o parejas a bordo. |
| `Parch` | Entero | Número de padres, madres, hijos o hijas a bordo. |
| `Ticket` | Texto | Código o número del tiquete. |
| `Fare` | Decimal | Tarifa pagada por el pasaje. |
| `Cabin` | Texto | Identificador de cabina. Presenta una cantidad importante de valores faltantes. |
| `Embarked` | Categórica | Puerto de embarque: `C` = Cherbourg, `Q` = Queenstown, `S` = Southampton. |

## Alcance del análisis

El proyecto contempla las siguientes actividades:

1. Identificar y documentar la fuente, formato y utilidad del dataset.
2. Incorporar el archivo original en `data/raw/` sin hacer cambios.
3. Inspeccionar el número de filas, columnas, nombres, tipos de datos y calidad inicial.
4. Detectar valores nulos y cuantificarlos por columna.
5. Limpiar datos e imputar valores faltantes con criterios documentados.
6. Identificar y tratar registros duplicados.
7. Estandarizar nombres de columnas, formatos de fecha si aplica, textos y categorías.
8. Analizar distribuciones de variables numéricas y categóricas e identificar valores atípicos.
9. Calcular e interpretar correlaciones entre variables numéricas relevantes.
10. Aplicar PCA a variables numéricas preparadas y evaluar la varianza explicada.

## Tratamiento previsto de calidad

La estrategia definitiva se definirá después de inspeccionar el archivo, pero se contemplan los siguientes controles:

| Situación | Tratamiento previsto |
|---|---|
| Valores nulos en `Age` | Imputar usando la mediana global o la mediana por grupos relevantes, por ejemplo, clase y sexo. |
| Valores nulos en `Embarked` | Imputar con la categoría más frecuente o documentar la regla aplicada. |
| Valores nulos en `Cabin` | Crear una categoría como `Unknown`, extraer la cubierta cuando sea útil o excluir la columna si su ausencia limita el análisis. |
| Registros duplicados | Identificar duplicados completos y validar la unicidad de `PassengerId`. |
| Nombres de columnas | Convertir a un formato uniforme, por ejemplo, minúsculas y `snake_case`. |
| Variables categóricas | Normalizar espacios y valores antes del análisis. |
| Valores atípicos | Revisar especialmente `Age` y `Fare`; conservarlos, transformarlos o tratarlos solo con una justificación documentada. |

## Análisis exploratorio esperado

El análisis exploratorio incluirá, como mínimo:

- Estadísticas descriptivas de variables numéricas: media, mediana, mínimo, máximo, desviación estándar y percentiles.
- Distribución de edad, tarifa y tamaño de familia.
- Frecuencias de sexo, clase de pasajero, puerto de embarque y supervivencia.
- Comparación de supervivencia por sexo, clase y puerto de embarque.
- Identificación visual de valores atípicos mediante histogramas y diagramas de caja.
- Matriz de correlación de variables numéricas relevantes.
- Evaluación de PCA después de seleccionar, limpiar, codificar y estandarizar las variables requeridas.

## Consideraciones para PCA

PCA se aplicará únicamente después de preparar los datos. El procedimiento incluirá:

1. Seleccionar variables numéricas relevantes.
2. Tratar valores faltantes.
3. Codificar variables categóricas si se incluyen en el análisis.
4. Estandarizar las variables para que las escalas no influyan de manera desproporcionada.
5. Calcular la varianza explicada por cada componente y su acumulado.
6. Determinar el número de componentes que resume la información con una pérdida aceptable.

La reducción de dimensionalidad será interpretada como una herramienta exploratoria; no se asumirá que los componentes principales representan causalidad.

## Historias de usuario

| ID | Historia de usuario | Resultado esperado |
|---:|---|---|
| 1 | Identificar fuentes de datos | Fuente, formato y propósito del dataset documentados. |
| 2 | Incorporar dataset original | Archivo original almacenado sin cambios en `data/raw/`. |
| 3 | Inspeccionar estructura del dataset | Filas, columnas, tipos y problemas iniciales identificados. |
| 4 | Detectar valores nulos | Valores faltantes cuantificados y documentados. |
| 5 | Limpiar e imputar datos | Dataset preparado mediante reglas de limpieza justificadas. |
| 6 | Validar duplicados | Registros duplicados identificados y tratados. |
| 7 | Normalizar formatos | Columnas, textos y categorías estandarizados. |
| 8 | Analizar distribuciones | Estadísticas, frecuencias y valores atípicos analizados. |
| 9 | Analizar correlaciones | Relaciones entre variables numéricas calculadas e interpretadas. |
| 10 | Explorar reducción de dimensionalidad | PCA aplicado y varianza explicada evaluada. |

## Tecnologías sugeridas

- Python 3
- Jupyter Notebook
- pandas
- NumPy
- Matplotlib
- Seaborn
- scikit-learn
- pytest, opcionalmente, para validaciones automatizadas

## Reglas de gestión de datos

- No modificar directamente los archivos ubicados en `data/raw/`.
- Guardar los resultados de limpieza en `data/processed/`.
- Documentar las decisiones de limpieza, imputación y eliminación de registros.
- Mantener código reproducible en notebooks o scripts dentro de `src/`.
- Usar nombres descriptivos para archivos, notebooks y resultados.
- Registrar hallazgos relevantes sobre calidad y limitaciones de los datos.

## Limitaciones del dataset

- El dataset contiene datos faltantes, en especial en `Cabin` y `Age`.
- La información representa únicamente a los pasajeros incluidos en el conjunto disponible, por lo que no debe generalizarse sin precaución.
- Algunas variables, como nombre y tiquete, requieren transformación adicional para análisis cuantitativo.
- Las asociaciones encontradas en el análisis no demuestran relaciones causales.

## Resultados esperados

Al finalizar el proyecto se espera contar con:

- El dataset original preservado en `data/raw/`.
- Un dataset limpio y documentado en `data/processed/`.
- Un notebook o script de análisis exploratorio.
- Visualizaciones de distribuciones, valores atípicos y correlaciones.
- Una evaluación de la viabilidad de PCA para resumir las variables seleccionadas.
- Conclusiones sobre las características asociadas con la supervivencia de los pasajeros.

## Fuente del dataset

El dataset puede consultarse y descargarse desde [Kaggle: Titanic - Machine Learning from Disaster](https://www.kaggle.com/competitions/titanic/data). También existen versiones públicas del conjunto Titanic en repositorios educativos y de ciencia de datos.