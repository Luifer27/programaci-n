import streamlit as st

# Mensaje de bienvenida inicial
st.image('https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png', width=200)
st.title('¡Bienvenido a tu primera app con Streamlit!')
st.markdown('''
<div style="background-color:#dbeafe;padding:15px;border-radius:10px;">
<h3>¡Hola! 👋</h3>
<p>Esta es una aplicación web interactiva donde puedes probar funcionalidades básicas de Streamlit.<br>
Por favor, ingresa tus datos para comenzar.</p>
</div>
''', unsafe_allow_html=True)

st.header('Entrada de usuario')
nombre = st.text_input('¿Cuál es tu nombre?')
edad = st.number_input('¿Cuál es tu edad?', min_value=0, max_value=120, step=1)

if nombre and edad:
    st.success(f'¡Hola, {nombre}! Tienes {edad} años.\n\nGracias por usar esta app. Aquí podrás realizar operaciones y ver resultados personalizados.')
elif nombre:
    st.info(f'Hola {nombre}, por favor ingresa tu edad para continuar.')
elif edad:
    st.info('Por favor, ingresa tu nombre para continuar.')

st.header('Cálculo rápido')
a = st.number_input('Ingresa un número', value=0, key='a')
b = st.number_input('Ingresa otro número', value=0, key='b')
if st.button('Sumar'):
    st.write(f'La suma es: {a + b}')

