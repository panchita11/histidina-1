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
    st.write("""
   La histidina es uno de los 22 aminoácidos proteinogénicos, aquellos que codifican nuestro código genético y son utilizados para la síntesis de proteínas. Además es considerado uno de los 9 aminoácidos esenciales que requerimos consumir a través de la dieta para evitar sufrir signos de degradación proteica y malnutrición.""")
    st.image(
        "https://thumbs.dreamstime.com/b/f%C3%B3rmula-qu%C3%ADmica-de-histidina-estructura-molecular-ilustraci%C3%B3n-vectorial-aislada-en-fondo-blanco-238646983.jpg",
        caption="Estructura molecular de la histidina",
        width=300
    )
