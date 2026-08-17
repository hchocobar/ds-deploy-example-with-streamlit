# Análisis Inmobiliario Interactivo con Streamlit

Aplicación de análisis exploratorio e interactivo de datos inmobiliarios desarrollada con **Python**, **Pandas**, **Plotly** y **Streamlit**.

El proyecto permite cargar un dataset procesado de propiedades inmobiliarias, aplicar filtros dinámicos, consultar estadísticas descriptivas y visualizar relaciones entre variables mediante gráficos interactivos.

## Aplicación publicada

La aplicación se encuentra desplegada en Streamlit Community Cloud:

[https://ds-deploy-example-with-app-mzxmyzjrcthhmkb8tq9wp4.streamlit.app/](https://ds-deploy-example-with-app-mzxmyzjrcthhmkb8tq9wp4.streamlit.app/)

## Objetivo del proyecto

El objetivo principal es construir una aplicación interactiva que permita explorar datos inmobiliarios de forma visual y dinámica.

El proyecto contempla dos etapas principales:

1. **Preparación y análisis de datos**
   - Carga del dataset original.
   - Limpieza y transformación de los datos con Pandas.
   - Generación de un archivo CSV procesado para ser utilizado por la aplicación.

2. **Aplicación interactiva**
   - Desarrollo de una interfaz web con Streamlit.
   - Filtros dinámicos desde la barra lateral.
   - Estadísticas descriptivas del dataset filtrado.
   - Visualizaciones interactivas con Plotly.
   - Visualización geográfica mediante mapa.

## Estructura del proyecto
```
text
.
├── app.py
├── requirements.txt
├── data
│   ├── raw
│   │   └── dataset original
│   └── processed
│       └── real_estate.csv
└── notebooks
    └── practice.ipynb
```
## Archivos principales

### `app.py`

Contiene la aplicación principal desarrollada con Streamlit.

La aplicación realiza las siguientes tareas:

- Carga el archivo procesado `data/processed/real_estate.csv`.
- Convierte columnas numéricas relevantes al tipo adecuado.
- Permite filtrar datos mediante un selector de columna y un rango de valores.
- Muestra los registros filtrados.
- Calcula estadísticas descriptivas:
  - Media.
  - Mediana.
  - Desviación estándar.
  - Mínimo.
  - Máximo.
  - Rango.
  - Cuartiles.
- Genera visualizaciones dinámicas:
  - Histograma de la variable seleccionada.
  - Gráfico de dispersión entre dos variables.
  - Línea de tendencia mediante regresión OLS.
  - Mapa geográfico cuando existen coordenadas de latitud y longitud.

### `notebooks/practice.ipynb`

Notebook utilizado para la fase inicial del proyecto.

Incluye el trabajo de:

- Carga del dataset original.
- Exploración inicial de los datos.
- Limpieza y preparación del DataFrame.
- Exportación del dataset procesado al directorio `data/processed`.

### `data/processed/real_estate.csv`

Archivo CSV utilizado por la aplicación Streamlit.

Contiene el dataset inmobiliario ya preparado para el análisis interactivo.

### `requirements.txt`

Listado de dependencias necesarias para ejecutar el proyecto.

Incluye:

- `numpy`
- `pandas`
- `matplotlib`
- `plotly`
- `scikit-learn`
- `streamlit`
- `statsmodels`

## Funcionalidades de la aplicación

## Panel lateral de filtros

La aplicación incluye un panel lateral desde el cual el usuario puede:

- Seleccionar una columna numérica para filtrar.
- Definir un rango de valores mediante un slider.
- Actualizar automáticamente los datos, estadísticas y gráficos según el filtro aplicado.

## Datos filtrados

Después de aplicar los filtros, la aplicación muestra:

- Cantidad de registros encontrados.
- Tabla interactiva con los datos filtrados.

## Resumen descriptivo

La aplicación calcula un resumen estadístico de las columnas numéricas disponibles, incluyendo:

- Media.
- Mediana.
- Desviación estándar.
- Valor mínimo.
- Valor máximo.
- Rango.
- Primer cuartil.
- Segundo cuartil.
- Tercer cuartil.

## Visualizaciones

### Histograma

Permite visualizar la distribución de una variable numérica seleccionada por el usuario.

Por defecto, si la columna `price` está disponible, se utiliza como variable objetivo inicial.

### Gráfico de dispersión

Permite analizar la relación entre dos variables numéricas.

El gráfico incluye una línea de tendencia calculada mediante regresión OLS.

### Mapa geográfico

Si el dataset contiene columnas de latitud y longitud, la aplicación muestra un mapa con la ubicación de las propiedades filtradas.

## Tecnologías utilizadas

- Python
- Pandas
- NumPy
- Plotly
- Streamlit
- Statsmodels
- Scikit-learn
- Matplotlib
- Jupyter Notebook

## Instalación local

Para ejecutar el proyecto en tu propio equipo, primero clona el repositorio y entra en la carpeta del proyecto.

Luego instala las dependencias:
```
bash
pip install -r requirements.txt
```
## Ejecución local

Para iniciar la aplicación Streamlit, ejecuta:
```
bash
streamlit run app.py
```
Después de ejecutar el comando, Streamlit mostrará una URL local similar a:
```
text
http://localhost:8501
```
Abre esa dirección en tu navegador para utilizar la aplicación.

## Flujo de trabajo recomendado

1. Revisar o ejecutar el notebook `notebooks/practice.ipynb`.
2. Verificar que el archivo procesado exista en `data/processed/real_estate.csv`.
3. Instalar las dependencias del proyecto.
4. Ejecutar la aplicación con Streamlit.
5. Explorar los datos mediante filtros, estadísticas y gráficos.
6. Consultar la versión publicada en Streamlit Community Cloud.

## Despliegue

La aplicación fue desplegada en **Streamlit Community Cloud**.

URL pública:

[https://ds-deploy-example-with-app-mzxmyzjrcthhmkb8tq9wp4.streamlit.app/](https://ds-deploy-example-with-app-mzxmyzjrcthhmkb8tq9wp4.streamlit.app/)

## Entrega del proyecto

La entrega del proyecto incluye:

- Repositorio con el código fuente.
- Notebook de análisis y preparación de datos.
- Aplicación Streamlit funcional.
- Archivo de dependencias.
- Aplicación publicada en la nube.
