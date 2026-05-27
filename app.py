import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Análisis Inmobiliario Interactivo",
                   page_icon="🏠",
                   layout="wide")



df = pd.read_csv("data/processed/real_estate.csv", sep=";", decimal=",")
df = df.drop(columns=[df.columns[0]], errors="ignore")

columnas_numericas = ["rooms", "bathrooms", "surface", "price", "latitude", "longitude"]

for columna in columnas_numericas:
    if columna in df.columns:
        df[columna] = pd.to_numeric(df[columna], errors="coerce")


st.title("🏠 Análisis Inmobiliario Interactivo")
st.markdown("""
Aplicación interactiva para realizar un análisis descriptivo y visual de propiedades inmobiliarias.
Los gráficos y estadísticas se actualizan automáticamente según los filtros seleccionados.
""")

columnas_numericas = ["rooms", "bathrooms", "surface", "price", "latitude", "longitude"]
columnas_numericas = [columna for columna in columnas_numericas if columna in df.columns]

st.sidebar.markdown("""
# Panel de control

Utiliza los filtros siguientes para explorar el dataset inmobiliario.

Los resultados, estadísticas y gráficos se actualizarán con base en los datos filtrados.
""")

columna_filtro = st.sidebar.selectbox("Selecciona la columna para filtrar", columnas_numericas)

valor_minimo = float(df[columna_filtro].min())
valor_maximo = float(df[columna_filtro].max())

rango_seleccionado = st.sidebar.slider("Selecciona el rango de valores",
                                       min_value=valor_minimo,
                                       max_value=valor_maximo,
                                       value=(valor_minimo, valor_maximo))

df_filtrado = df[(df[columna_filtro] >= rango_seleccionado[0]) & (df[columna_filtro] <= rango_seleccionado[1])]

st.subheader("Datos filtrados")
st.write(f"Registros encontrados: **{df_filtrado.shape[0]}**")
st.dataframe(df_filtrado)

st.subheader("Resumen descriptivo")

columnas_numericas_filtradas = df_filtrado[columnas_numericas]

resumen = pd.DataFrame({"Media": columnas_numericas_filtradas.mean(),
                        "Mediana": columnas_numericas_filtradas.median(),
                        "Desviación estándar": columnas_numericas_filtradas.std(),
                        "Mínimo": columnas_numericas_filtradas.min(),
                        "Máximo": columnas_numericas_filtradas.max(),
                        "Rango": columnas_numericas_filtradas.max() - columnas_numericas_filtradas.min(),
                        "Q1": columnas_numericas_filtradas.quantile(0.25),
                        "Q2": columnas_numericas_filtradas.quantile(0.50),
                        "Q3": columnas_numericas_filtradas.quantile(0.75)})

st.dataframe(resumen)

st.subheader("Visualización dinámica")

if df_filtrado.empty:
    st.warning("No hay datos disponibles con los filtros seleccionados.")
else:
    columna_target = st.selectbox("Selecciona la variable objetivo para el histograma",
                                  columnas_numericas,
                                  index=columnas_numericas.index("price") if "price" in columnas_numericas else 0)

    fig_histograma = px.histogram(df_filtrado,
                                  x=columna_target,
                                  nbins=30,
                                  title=f"Distribución de {columna_target}",
                                  labels={columna_target: columna_target.capitalize()})

    fig_histograma.update_layout(xaxis_title=columna_target.capitalize(),
                                 yaxis_title="Frecuencia")

    st.plotly_chart(fig_histograma, use_container_width=True)

    st.subheader("Gráfico de dispersión")

    columnas_scatter = [columna for columna in columnas_numericas if columna not in ["latitude", "longitude"]]

    columna_x = st.selectbox("Selecciona la variable del eje X",
                             columnas_scatter,
                             index=columnas_scatter.index("surface") if "surface" in columnas_scatter else 0)

    columna_y = st.selectbox("Selecciona la variable del eje Y",
                             columnas_scatter,
                             index=columnas_scatter.index("price") if "price" in columnas_scatter else 0)

    fig_scatter = px.scatter(df_filtrado,
                             x=columna_x,
                             y=columna_y,
                             title=f"Relación entre {columna_x} y {columna_y}",
                             labels={columna_x: columna_x.capitalize(),
                                     columna_y: columna_y.capitalize()},
                             trendline="ols")

    fig_scatter.update_layout(xaxis_title=columna_x.capitalize(),
                              yaxis_title=columna_y.capitalize())

    st.plotly_chart(fig_scatter, use_container_width=True)

    if {"latitude", "longitude"}.issubset(df_filtrado.columns):
        st.subheader("Mapa geográfico")

        df_mapa = df_filtrado.dropna(subset=["latitude", "longitude"])

        if df_mapa.empty:
            st.info("No hay coordenadas disponibles para mostrar el mapa con los filtros actuales.")
        else:
            st.map(df_mapa.rename(columns={"latitude": "lat", "longitude": "lon"}))