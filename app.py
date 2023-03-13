import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
df = pd.read_csv(
    'https://raw.githubusercontent.com/reisanar/datasets/master/LaLiga.csv')

# Crear el título y la descripción de la página
st.title('La Liga')

st.write('Esta página muestra datos de las temporada de La Liga desde 1970 hasta 2017 y permite a los usuarios filtrarlos y visualizarlos.')

# Agregar widgets para filtrar los datos
st.sidebar.header("Porfavor, filtre aquí los datos que desea visualizar: ")

points_filter = st.sidebar.slider('Filtrar por puntos en la temporada', 0, 100, (0, 100))
home_win_filter = st.sidebar.number_input('Introduce un número de victorias en casa', 0, 20, 0)

club = st.sidebar.multiselect(
            "Selecciona el equipo:",   
            options = df['club'].unique()
        )

season = st.sidebar.multiselect(
            "Selecciona la temporada:",   
            options = df['season'].unique(),
            default = df['season'].unique()
        )

df = df.query(
    "club == @club & season == @season"
)

# Filtrar los datos
df = df[(df['points'] >= points_filter[0]) & (df['points'] <= points_filter[1])]
df = df[df['home_win'] >= home_win_filter]

# KPI de puntos
st.title(":bar_chart: Datos sobre partidos y puntos totales")
st.markdown("##")

total_matches = int(df['total_matches'].sum())
points = int(df['points'].sum())

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total de partidos")
    st.subheader(f"⚽  {total_matches:,}")

with right_column:
    st.subheader("Total de puntos")
    st.subheader(f" 🎖️  {points:,}")

st.markdown("---")

# Crear el gráfico de barras con Matplotlib
fig, ax = plt.subplots()
ax.barh(df['club'], df['goals_scored'])

# Establecer los títulos y etiquetas de los ejes
ax.set_title('Goles marcados por equipo')
ax.set_xlabel('Goles marcados')
ax.set_ylabel('Equipos')

# Mostrar el dataframe filtrado
st.write('Datos filtrados:')
st.dataframe(df)

# Mostrar el gráfico de barras
st.pyplot(fig)
