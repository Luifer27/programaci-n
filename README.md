

# programaci-n

## Introducción a GitHub Codespaces y Copilot

Este proyecto está diseñado para mostrar cómo puedes aprovechar GitHub Codespaces y GitHub Copilot en el desarrollo de aplicaciones Python:

- **GitHub Codespaces** te permite crear entornos de desarrollo completos en la nube, listos para programar sin necesidad de instalar nada en tu máquina local. Puedes abrir, editar, ejecutar y depurar tu código directamente desde el navegador o Visual Studio Code.

- **GitHub Copilot** es una herramienta de inteligencia artificial que te asiste mientras programas, sugiriendo líneas de código, funciones completas y ayudando a documentar o resolver problemas de programación de manera eficiente.

Este repositorio utiliza ambas herramientas para facilitar el aprendizaje y la experimentación con Python y Streamlit.

## Funcionalidades de la aplicación Streamlit

## Funcionalidades de la aplicación Streamlit

El archivo `app_streamlit.py` implementa una aplicación web interactiva con las siguientes características:

- **Mensaje de bienvenida:** Al iniciar la app, se muestra un mensaje visual y amigable para el usuario.
- **Entrada de usuario:**
  - Solicita el nombre del usuario.
  - Solicita la edad del usuario.
  - Muestra una respuesta personalizada y detallada según los datos ingresados.
- **Cálculo rápido:**
  - Permite ingresar dos números.
  - Al presionar el botón "Sumar", muestra el resultado de la suma.

## ¿Cómo ejecutar la app?

1. Activa el entorno virtual:
	```bash
	source .venv/bin/activate
	```
2. Instala las dependencias (si es necesario):
	```bash
	pip install streamlit
	```
3. Ejecuta la aplicación:
	```bash
	streamlit run app_streamlit.py
	```

Esto abrirá una página web local donde podrás interactuar con la app.
