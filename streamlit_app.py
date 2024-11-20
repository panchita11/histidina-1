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
    st.write("""La histidina (His, H) es un aminoácido que se utiliza para la síntesis de proteínas. Es una molécula hidrofílica, por lo que generalmente está orientada hacia la parte externa de las estructuras proteicas cuando estas se encuentran en un medio líquido.""")
 
