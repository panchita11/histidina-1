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
    st.image("https://th.bing.com/th/id/OIP.a1VjRkDwAYHh2KAOjC9NEQHaFj?w=226&h=180&c=7&r=0&o=5&pid=1.7")
    st.write("""La histidina cumple funciones fisiológicas muy importantes en el ser humano, como formar parte de los centros activos de muchas enzimas, participar en el crecimiento, en el sistema inmunitario y en la formación de la mielina en las fibras nerviosas, entre otras.""")
