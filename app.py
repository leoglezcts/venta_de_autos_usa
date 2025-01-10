import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv(r'C:\Users\lgonzalezc\Documents\TripleTen\Sprint7\venta_de_autos_usa\vehicles_us.csv') # leer los datos


st.header("Venta de Vehículos USA")

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

'''ESTADO DE LOS AUTOS '''

autos_condicion = df['condition'].value_counts().reset_index()
autos_condicion.columns = ['condition', 'count']

pie_button = st.button('Estado') # crear un botón
if pie_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Agrupación de los autos por su estado para comparar su condición')
    
    # crear un diagrama de dispersión
    fig4 = px.pie(autos_condicion, values='count', names='condition', 
         title='Estado de autos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig4, use_container_width=True)

'''TIPO DE TRANSMISIÓN'''

# conteo de los autos para comparar su transmisión
autos_transmisión = df['transmission'].value_counts().reset_index()
autos_transmisión.columns = ['transmission', 'count']


treemap_button = st.button('Transmisión') # crear un botón
if treemap_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Agrupación de los autos por su transmisión')
    
    # crear un diagrama de dispersión
    fig5 = px.treemap(autos_transmisión, path=['transmission'], names='transmission', values='count',
                 title='Transmisión de autos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig5, use_container_width=True)
