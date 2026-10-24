import streamlit as st
import pandas as pd

st.title("Sistema de Informe de Rendimiento Estudiantil")

uploaded_file = st.file_uploader("Carga tu archivo Excel aquí", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.write("Vista previa de los datos:", df.head())
    
    if 'Nota' in df.columns and 'Estudiante' in df.columns:
        bajos_rendimientos = df[df['Nota'] <= 20]
        
        st.header("Estudiantes con Nota Baja")
        
        for index, row in bajos_rendimientos.iterrows():
            st.warning(f"**Estudiante:** {row['Estudiante']} - **Nota:** {row['Nota']}")
            
            # Aquí se pueden agregar recomendaciones basadas en la materia o situación
            st.write("### Recomendaciones:")
            st.info("Se sugiere tutoría personalizada y revisión de las evaluaciones formativas previas.")
            st.write("---")
    else:
        st.error("Asegúrate de que el archivo tenga las columnas 'Estudiante' y 'Nota'")

