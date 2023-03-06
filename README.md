# 📈 Cuadro de mandos personal 📊
 
> Usa este repositorio para crear un cuadro de mandos personal con Streamlit. Documenta los siguientes apartados del README.
> Incluye en tu README la url de donde has publicado tu aplicación. Pon la `url` también en el `About` de tu repositorio.

## Objetivo
Diseño de un cuadro de mandos personal para visualización e interacción con un conjunto de datos.

## Los datos
He elegido el conjunto de datos de fútbol de La Liga de España de las temporadas 1970 hasta 2017, mostrando los datos de los equipos y sus victorias, goles a favor, en contra, etc.

## Búsqueda de los datos
Encontré los datos en github en un repositorio en formato csv.

## Documentación de los datos
Decidí utilizar datos de la temporada de fútbol de La Liga desde 1970 hasta 2017, sacados de github en formato csv. "https://github.com/reisanar/datasets/blob/master/LaLiga.csv"
Los campos son season(temporada), club(equipo), home_win(victorias en casa), away_win(victorias fuera de casa), home_loss(derrotas en casa), away_loss(derrotas fuera de casa), matches_won(partidos ganados), matches_lost(partidos perdidos), matches_drawn(partidos empatados), total_matches(partidos totales), points(puntos), home_goals(goles en casa), away_goals(goles fuera de casa), goals_scored(goles a favor), goals_conceded(goles en contra), goal_difference(diferencia de goles).

## Prepara tu aplicación.
La aplicación se llamará `app.py`. Añade un `requirements.txt` con las dependencias de tu aplicación. Ve actualizándolo a medida que vayas añadiendo librerías.

## Carga y análisis de conjunto de dato con pandas
Carga el conjunto de datos en un dataframe de pandas y realiza un análisis exploratorio de los datos.

## Visualización de los datos
Opté por utilizar matplotlib para la visualización de los datos en una gráfica horizontal de los goles a favor de cada equipo.

## Diseña la interacción que van a tener tus datos
Se pueden filtrar los datos según los puntos que hayan hecho en las temporadas mediante una barra slider,
también se puede introducir el número de victorias en casa que haya tenido el equipo, y se puede filtrar la selección por equipo y por temporada.
También se ven los partidos y los puntos totales de todas las temporadas juntas.

## Prepara la aplicación (cuadro de mandos) con Streamlit
Prepara y prueba la aplicación.

## Publica la aplicación.
Publica la aplicación en Streamlit Cloud, en Heroku o en el servicio que prefieras https://docs.streamlit.io/streamlit-community-cloud/get-started/deploy-an-app

Streamlit Cloud: https://aaronbresser-streamlit2-cuadro-mandos-app-8419rr.streamlit.app/
