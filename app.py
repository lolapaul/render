import streamlit as st

st.header('Lanzar una moneda')

number_of_trials = st.slider('¿Número de intentos?',1,1000,10)
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} inten    tos en curso.')
    
    st.write('Esta aplicación aún no es funcional. En c    onstrucción.')
