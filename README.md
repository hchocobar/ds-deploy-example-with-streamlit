# Proyecto

## Análisis Interactivo de Datos con Streamlit

**Objetivos:** 
- Realizar el Análisis Exploratorio de Datos (EDA) de un conjunto de datos utilizando **Pandas**.
- Desarrollar una aplicación interactiva en **Streamlit** que cargue y visualice un conjunto de datos estándar, aplicando conceptos de manipulación de datos con **Pandas** e integración de *widgets* interactivos.

## Dataset seleccionado

Utilizaremos el *dataset* del curso de Power BI modificado previamente por el profesor para contener los desafios necesarios para el Proyecto. 


## Actividades Requeridas del Proyecto

El proyecto se dividirá en dos fases:

La primera fase realizada en el archivo `practice.ipynb` consiste en:
- Carga y Preparación de Datos (Pandas en Jupyter Notebook), 
- Análisis Exploratorio de Datos (Pandas en Jupyter Notebook)
- Grabación del dataframe resultante en un archivo CSV

La segunda fase realizada en el archivo `app.py` consiste en:
- Análisis Descriptivo Interactivo (Streamlit), y 
- Visualización Dinámica (Streamlit).
- Despliegue en la Nube (Streamlit Community Cloud).

### Primera Fase

En el archivo `notebooks/practice.ipynb`: 

1. **Carga y Estructura:** Cargar el dataset que encontrarás en directorio `data/raw` y lo convertirás en un DataFrame de Pandas.
2. **EDA**: Realizar un Análisis Exploratorio de Datos (EDA) del DataFrame utilizando Pandas, límpiarlo para obtener un nuevo dataframe.
3. **Grabar**: Grabar el nuevo DataFrame en un archivo CSV con un nuevo nombre descriptivo en el directorio `data/processed`.

### Segunda Fase

En el archivo `app.py`:

#### Análisis Descriptivo Interactivo (Streamlit Widgets)
Esta fase se centra en usar los *widgets* de Streamlit para permitir al usuario explorar los datos.

1.  **Sidebar de Control (`st.sidebar`):**
    * Implementar un `st.sidebar.markdown()` para el título y descripción de los filtros.
2.  **Filtros (`st.slider`):**
    * Crear un **slider** que permita al usuario seleccionar un rango de alguna columna del DataFrame.
    * Rango: El rango del slider debe ir desde el mínimo hasta el máximo de la columna.
    * Filtrar el DataFrame para incluir solo los registros cuyo valor se encuentre dentro del rango seleccionado por el usuario.
3.  **Resumen Descriptivo:**
    * Mostrar la mediana y el rango (Máximo - Mínimo), la media, desviación estándar y los quartiles de las columnas del DataFrame resultante después de aplicar todos los filtros.

#### Visualización Dinámica

Deberás mostrar la relación entre las variables utilizando gráficos que se actualicen automáticamente con los filtros anteriores.

1.  **Gráfico de Distribución del Target (`st.pyplot` o `st.plotly_chart`):**
    * Crear un **histograma** de la variable objetivo utilizando una librería externa (como Matplotlib o Plotly).
    * **Requisito:** El gráfico debe reflejar la distribución de los datos **después** de aplicar los filtros del usuario.
2.  **Gráfico de Dispersión (Regresión):**
    * Crear un gráfico de dispersión (scatter plot) que muestre la relación entre dos columnas del DataFrame.
    * **Requisito:** Este gráfico también debe actualizarse con los datos filtrados y ser lo suficientemente informativo (ej. incluir etiquetas y un título).
3.  ** Opcional - Mapa Geográfico** (Streamlit Nativo o Plotly):
    * Si tu Dataset contiene valores de longitud y latitud utiliza la función nativa de Streamlit (st.map()) o un gráfico de dispersión de Plotly con st.plotly_chart() para mapear los valores de algunas columnas.
    * Requisito: El mapa debe mostrar la distribución geográfica de los valores filtrados por el usuario.

---

#### Despliegue en la Nube

Deberás preparar tu proyecto para el despliegue.

1.  **Git/GitHub:** Crear un **repositorio público** en GitHub a partir de este template.

2.  **Estructura de Carpeta:**
    * `app.py` (código de Streamlit).
    * `notebooks/practice.ipynb` en este archivo puedes realizar un análisis previo del dataset propuesto
    * `requirements.txt` (listado de dependencias: `streamlit`, `pandas`, `scikit-learn`, `matplotlib` o `plotly`).

3.  **Despliegue:** Desplegar la aplicación final utilizando **Streamlit Community Cloud** (share.streamlit.io).

## Entrega

Deberás entregar:
- el **enlace al repositorio de GitHub**.
- el **enlace a la aplicación desplegada**

## How to run it on your own machine
1. Install the requirements

```bash
$ pip install -r requirements.txt
```
2. Run the app

```bash
$ streamlit run app.py
```
