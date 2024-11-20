import streamlit as st

st.title("HISTIDINA")
st.sidebar.title("Menú de navegación")
st.sidebar.header("Secciones disponibles")

# Opciones en la barra lateral
opcion = st.sidebar.selectbox(
    "Selecciona una sección:",
    ["Información básica", "Funciones biológicas", "Propiedades químicas"]
)
# Contenido dinámico basado en la selección
if opcion == "Información básica":
    st.header("Información básica sobre la Histidina")
    st.write("""
    La histidina es un aminoácido esencial que desempeña un papel crucial en 
    varias funciones biológicas. Su fórmula química es **C₆H₉N₃O₂** y es conocida 
    por ser precursora de la histamina.
    """)
    st.wride("""En la naturaleza encontramos el enantiómero levorrotarorio de la histidina, es decir, la forma L-histidina.

Tanto de origen animal como vegetal, por lo que su carencia es una condición extraña y normalmente asociada a alteraciones genéticas o malnutrición severa.""")
    st.write("""En la naturaleza encontramos el enantiómero levorrotarorio de la histidina, es decir, la forma L-histidina.""")
    st.image("https://arribasalud.com/wp-content/uploads/2018/02/histidina-665x285.jpg")
