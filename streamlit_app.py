import streamlit as st

st.title("HISTIDINA👩🏻‍🔬")
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
    st.write("""La biosíntesis de la histidina es un proceso complejo que sucede principalmente en el hígado y que requiere de 9 a 11 pasos enzimáticos. Su degradación se produce en el hígado y la piel y pasa por la formación de glutamato, siguiendo luego diferentes vías.

Muchos alimentos son ricos en histidina, como las proteínas animales (carne y productos lácteos), y las proteínas vegetales. Estos aportan gran parte de los requerimientos diarios de histidina que el cuerpo necesita para funcionar correctamente.

El déficit o el exceso de histidina ocasionado por problemas hereditarios metabólicos o de transporte, o la falla dietética en la ingesta, se relacionan con algunos problemas importantes que afectan la salud en niños y en adultos. El consumo suficiente de histidina permite mantener una vida sana y saludable en la mayor parte de los casos.""")
    st.image("""https://draxe.com/wp-content/uploads/2019/06/histidine-header-768x350.jpg""")
elif opcion == "Funciones biológicas":
   st.header("Funciones biologicas de la Histidina")
   st.write("""La histidina cumple varias funciones biológicas esenciales en el cuerpo humano debido a su estructura química única, que incluye un anillo imidazol capaz de participar en diversas reacciones químicas. Aquí están sus principales funciones:""")
   st.image("https://www.mismumi.com/wp-content/uploads/histidina-aminoacido-funcion-336x205.jpg")
   st.write("""1. Regulación del pH 
El anillo imidazol de la histidina tiene un pKa cercano al pH fisiológico (~6.0), lo que le permite actuar como un regulador en los cambios de pH.  

 2. Precursor de la histamina
La histidina es el precursor de la histamina, una amina biológicamente activa con funciones importantes:  
- Sistema inmunológico: La histamina es liberada durante las reacciones alérgicas y juega un papel clave en la respuesta inflamatoria.  
- Sistema nervioso: Actúa como neurotransmisor en el cerebro.

3. Participación en reacciones enzimáticas
El grupo imidazol de la histidina es fundamental en muchas enzimas:  
- Actúa como donador o receptor de protones en reacciones catalíticas.  

 4. Unión y transporte de metales
La histidina es crucial en la unión de iones metálicos:  
- Hemoglobina y mioglobina: Participa en la unión del oxígeno a través de la interacción con el grupo hemo.  
- Forma complejos con otros metales como el zinc, el cobre y el hierro, esenciales para funciones enzimáticas y estructurales.

5. Rol en la estabilidad estructural de proteínas
Contribuye a la formación de:  
- Puentes de hidrógeno y enlaces no covalentes que estabilizan la estructura tridimensional de las proteínas.  
Es importante en proteínas como la colágena y en mecanismos de unión molecular.

 6.Producción de energía
En el metabolismo, la histidina puede ser degradada en el ciclo de los ácidos tricarboxílicos (ciclo de Krebs):  
- Se convierte en ácido glutámico y luego en α-cetoglutarato, un intermediario clave en la producción de energía celular.

7.Impulso nervioso y neurotransmisión  
- Como precursor de la histamina, tiene un rol en la transmisión sináptica en el cerebro, regulando el ciclo sueño-vigilia y la memoria.  
- También influye en procesos relacionados con la modulación de la excitabilidad neuronal.

8. Rol en el sistema inmunológico  
- Participa en la maduración y función de los glóbulos blancos.  
- Es esencial para la síntesis de proteínas involucradas en la respuesta inmune, como las inmunoglobulinas.""")
   st.image("data:image/jpeg;base64,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")
elif opcion == "Propiedades químicas":
    st.header("Propiedades químicas de la histidina")
    st.write("""La histidina es un aminoácido esencial con estas propiedades químicas principales:
1.	Fórmula química: C6H9N3O2

2.	Polar y básica: Su cadena lateral contiene un anillo de imidazol.

3.	pKa del imidazol: ~6.0, permitiendo actuar como ácido o base cerca del pH fisiológico.

4.	Capacidad de enlace: Forma enlaces de hidrógeno y se une a iones metálicos.

5.	Soluble en agua: Debido a su polaridad.

6.	Función bioquímica: Participa en la catálisis enzimática y actúa como tampón biológico.
""")
elif opcion == "Propiedades químicas":
    st.header("Propiedades químicas de la histidina")
    # Datos de pKa para la histidina y algunas otras proteínas
proteins = ["Histidina", "Aspartato", "Glutamato", "Cisteína", "Lysina"]
pKa_values = [6.0, 3.9, 4.2, 8.3, 10.5]

# Crear la interfaz de Streamlit
st.title("Comparación de pKa de la Histidina con Otras Proteínas")
st.write("A continuación se muestra una comparación sencilla de los valores de pKa de varios aminoácidos comunes.")

# Crear un gráfico de barras con Streamlit
st.bar_chart(data={"Proteínas": proteins, "pKa": pKa_values})

st.video("https://youtube.com/shorts/5xuA2aGRIVU?feature=shared")

st.image("https://th.bing.com/th/id/OIP.INVqNl-62twQfbS82hMmQgHaEn?rs=1&pid=ImgDetMain")
