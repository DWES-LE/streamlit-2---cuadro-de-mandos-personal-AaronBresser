import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

# Cargar los datos del archivo CSV
df = pd.read_csv(
    'https://raw.githubusercontent.com/reisanar/datasets/master/LaLiga.csv')

# Crear el título y la descripción de la página
st.title('La Liga')

st.write('Esta página muestra datos de las temporada de La Liga desde 1970 hasta 2017 y permite a los usuarios filtrarlos y visualizarlos.')

#columnas en español
df = df.rename(columns={
    "season": "Temporada",
    "club": "Equipo",
    "home_win": "Victorias locales",
    "away_win": "Victorias visitantes",
    "home_loss": "Derrotas locales",
    "away_loss": "Derrotas visitantes",
    "matches_won": "Victorias",
    "matches_lost": "Derrotas",
    "matches_draw": "Empates",
    "total_matches": "Partidos totales",
    "points": "Puntos",
    "home_goals": "Goles locales",
    "away_goals": "Goles visitantes",
    "goals_scored": "Goles marcados",
    "goals_conceded": "Goles encajados",
    "goal_difference": "Diferencia de goles"
})

# KPI de puntos
st.title(":bar_chart: Datos sobre partidos y puntos totales")
st.markdown("##")

total_matches = int(df['Partidos totales'].sum())
points = int(df['Puntos'].sum())

left_column, right_column = st.columns(2)
with left_column:
    st.subheader("Total de partidos")
    st.subheader(f"⚽  {total_matches:,}")

with right_column:
    st.subheader("Total de puntos")
    st.subheader(f" 🎖️  {points:,}")

st.markdown("---")

# Agregar widgets para filtrar los datos
st.sidebar.header("Porfavor, filtre aquí los datos que desea visualizar: ")

puntos_min = st.sidebar.slider('Puntos mínimos', min_value=0, max_value=int(df['Puntos'].max()))
puntos_max = st.sidebar.slider('Puntos máximos', min_value=0, max_value=int(df['Puntos'].max()), value=int(df['Puntos'].max()))
df = df[(df['Puntos'] >= puntos_min) & (df['Puntos'] <= puntos_max)]

#Tabla con los equipos con más puntos por temporada
st.write("Equipos con más puntos por temporada (15 primeros):")
tabla_puntos = df[["Temporada", "Equipo", "Puntos"]].sort_values(by="Puntos", ascending=False).head(15)
st.table(tabla_puntos)

#Gráfico de dispersión entre goles marcados por temporada
st.write("Relación entre goles marcados y las temporadas:")
grafico_golestempo = df.plot(kind="scatter", x="Goles marcados", y="Temporada")
st.pyplot(grafico_golestempo.get_figure())

st.markdown("---")

# Equipos que más aparecen por temporada
top_equipos = df['Equipo'].str.split(', ').explode().value_counts().head(10)

# Renombro las columnas
top_equipos = top_equipos.rename_axis('Equipos').reset_index(name='Temporadas Disputadas')


st.title("Top 10 Equipos con más temporadas disputadas")
st.table(top_equipos)

# Respectivo gráfico de barras sobre los equipos con más temporadas disputadas
st.write("Equipos con más temporadas disputadas")
grafico_equipostempo = alt.Chart(top_equipos).mark_bar().encode(
    x="Temporadas Disputadas",
    y=alt.Y("Equipos", sort="-x"),
    color="Temporadas Disputadas"
)
st.altair_chart(grafico_equipostempo, use_container_width=True)

st.markdown("---")

# Cantidad de equipos y temporadas disputadas
equipos = df['Equipo'].str.split(', ').explode().value_counts()

# Gráfico de pastel según equipos y temporadas disputadas
grafico_equipostmp = alt.Chart(equipos.reset_index()).mark_arc().encode(
    theta='Equipo:Q',
    color='index:N',
    tooltip=['index:N', 'Equipo:Q']
).properties(
    width=500,
    height=500
)

st.write("Temporadas disputadas según todos los equipos:")
st.altair_chart(grafico_equipostmp, use_container_width=True)

st.markdown("---")

# Agrupar las temporadas por año y encontrar la diferencia de goles más alta
idx = df.groupby('Temporada')['Diferencia de goles'].idxmax()

# Tabla original y ordenarlas por temporada
top_movies = df.loc[idx, ['Temporada', 'Equipo', 'Diferencia de goles']].sort_values('Temporada')

#la columna Calificación a 2 decimales
top_movies['Diferencia de goles'] = top_movies['Diferencia de goles']

st.write("Equipo con mayor diferencia de goles por temporada:")
st.table(top_movies)

st.markdown("---")

#Lista con todos los equipos
equipos1 = sorted(df['Equipo'].unique())

#Selector de equipo
equipo_seleccionado = st.selectbox('Selecciona un equipo', equipos1)

# Filtrado según selección del usuario
df_filtrado = df[df['Equipo'] == equipo_seleccionado]

# Obtener
equipos1 = df_filtrado['Temporada'].tolist()

st.write('Equipo: ', equipo_seleccionado)
st.table(df_filtrado[['Temporada', 'Victorias', 'Derrotas']])

st.markdown("---")

#Lista con todas las temporadas
temporadas = sorted(df['Temporada'].unique())

#Selector de temporada
temporada_seleccionada = st.selectbox('Seleccione una temporada', temporadas)

# Filtrado según selección del usuario
df_filtrado = df[df['Temporada'] == temporada_seleccionada]

#Tabla con los puntos de cada equipo en x temporada
st.table(df_filtrado[['Equipo', 'Puntos']].sort_values('Puntos', ascending=False))

st.markdown("---")
st.markdown("---")

# Mostrar el dataframe filtrado
st.write('Datos filtrados por el usuario:')
st.dataframe(df)

st.sidebar.title("Número de goles encajados por cada equipo en una temporada (se mostrará la tabla al final)")
goles_input = st.sidebar.text_input("Introduce número de goles encajados: ")

#Introduce un número
try:
    goles = int(goles_input)
except ValueError:
    st.stop()

# Filtrar los datos según el número de goles encajados introducido por el usuario
filtered_data = df[df['Goles encajados'] == goles]

# Tabla con los equipos que han recibido x goles en temporadas
if not filtered_data.empty:
    st.title("Equipos que han encajado " + str(goles) + " goles")
    st.write(filtered_data[["Temporada", "Equipo"]])
else:
    st.title("No han encajado tantos goles: " + str(goles))


