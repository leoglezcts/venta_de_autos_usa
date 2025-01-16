import pandas as pd
from matplotlib import pyplot as plt
import plotly.express as px
import streamlit as st
import missingno as msno

# lectura de DataFrame
df = pd.read_csv(r'vehicles_us.csv') # leer los datos

# titulos
st.header("Venta de Vehículos USA")
st.subheader('Análisis exploratorio de datos')
st.dataframe(df.head())
st.write("Previsualización de DataFrame")

# mostrar valores nulos en el DF
msno_button = st.button('Valores nulos')
if msno_button:
    # Mostrar porcentaje de valores nulos
    null_percent = df.isnull().mean() * 100
    null_percent_formatted = null_percent.apply(lambda x: f"{int(round(x))}%")
    sorted_null_percent = null_percent.sort_values(ascending=False)
    df_sorted = df[sorted_null_percent.index]

    st.write("Porcentaje de valores nulos por columna:")
    st.dataframe(null_percent_formatted.rename('Porcentaje').round(0))

# Generar y mostrar el gráfico de barras de los valores nulos
    st.write("Gráfico de barras de de valores nulos:")
    fig, ax = plt.subplots(figsize=(10, 6))
    msno.bar(df_sorted, ax=ax)
    st.pyplot(fig)
    st.write("Como se observa en el gráfico el campo con más valores nulos es el campo de 'is_4wd', seguido de el color de la pintura y el odometro.")

'''KILOMETRAJE DE TODOS LOS AUTOS '''


hist_button_general = st.button('Dispersión de KM General') # crear un botón
if hist_button_general: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Dispersión del kilometraje en base a todos los vehículos.')
    
    # crear un histograma
    fig = px.histogram(df, x="odometer")
    fig.update_xaxes(range = [0, 500000])

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    st.write("Se observa una distribución con sesgo positivo, en la cual la mayoría de los vehículos presentan un kilometraje aproximado entre 98,000 y 122,000 kilómetros. A continuación, procederé a elaborar un gráfico de caja para visualizar de manera más clara la concentración de los datos.")

'''KILOMETRAJE DE LOS AUTOS POR MARCA'''
df['brand'] = df['model'].str.split(' ').str.get(0)

hist_button_brand = st.button('Dispersión de KM por Marcas') # crear un botón
if hist_button_brand: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Dispersión del kilometraje en base a las marcas de los vehículos.')
    
    # crear un histograma
    fig2 = px.box(df, y="odometer", x = 'brand',title= "Kilometraje de autos")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
    st.write("Las marcas que tienen un menor kilometraje en base a su mediana es Nissan y Volkswagen. Cabe destacar que los datos del odometro de la marca mercedes-benz no se registraron.")


'''PRECIO DE LOS AUTOS POR CLASIFICACIÓN '''

scatter_button = st.button('Precio') # crear un botón
if scatter_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Muestra el precio de los autos de acuerdo a su clasificación')
    
    # crear un diagrama de dispersión
    fig3 = px.strip(df, x = 'price', hover_name= 'model', color = 'type', 
         title= 'Precio de autos de acuerdo a su categoría')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig3, use_container_width=True)
    st.write("Se observa una distribución con sesgo positivo, en la cual la mayoría de los vehículos presentan un kilometraje aproximado entre 98,000 y 122,000 kilómetros. A continuación, procederé a elaborar un gráfico de caja para visualizar de manera más clara la concentración de los datos.")

'''ESTADO DE LOS AUTOS '''

autos_condicion = df['condition'].value_counts().reset_index()
autos_condicion.columns = ['condition', 'count']

pie_button = st.button('Estado') # crear un botón
if pie_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Agrupación de los autos por su estado para comparar su condición'
            )
    
    # crear un diagrama de dispersión
    fig4 = px.pie(autos_condicion, values='count', names='condition', 
         title='Estado de autos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig4, use_container_width=True)
    st.write(
        "La mayoría de los autos en este dataset son autos en buena condición."
        )
'''TIPO DE TRANSMISIÓN'''

# conteo de los autos para comparar su transmisión
autos_transmisión = df['transmission'].value_counts().reset_index()
autos_transmisión.columns = ['transmission', 'count']

# calcular el porcentaje de cada categoría
autos_transmisión['percentage'] = (autos_transmisión['count'] / autos_transmisión['count'].sum()) * 100
autos_transmisión['label'] = autos_transmisión.apply(
    lambda row: f"{row['transmission']} ({row['percentage']:.1f}%)", axis=1
)
# botón 
treemap_button = st.button('Transmisión') # crear un botón
if treemap_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Agrupación de los autos por su transmisión')
    
    # Crear un Treemap con etiquetas que incluyan los porcentajes
    fig5 = px.treemap(
        autos_transmisión,
        path=['label'],  # Usar las etiquetas con los porcentajes
        values='count',
        title='Transmisión de autos'
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig5, use_container_width=True)
    st.write("El 91% de los vehículos son automaticos, solo el 3.5% pertencen a una caja de velocidades diferente a las convencionales")
