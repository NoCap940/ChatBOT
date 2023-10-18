import b_backend
import streamlit as st
from streamlit_chat import message

st.title("App Chatbot")
st.write("Preguntas, dudas, consultas...")

# Lista para almacenar los mensajes del chat
messages = []

# Actualizar la función `click()` para agregar los mensajes a la lista
def click():
    if st.session_state.user != '':
        pregunta = st.session_state.user
        respuesta = b_backend.consulta(pregunta)

        # Agregar los mensajes a la lista
        messages.append({"role": "user", "content": pregunta})
        messages.append({"role": "bot", "content": respuesta})

        # Limpiar el input de usuario después de enviar la pregunta
        st.session_state.user = pregunta

# Actualizar el bucle `for` para mostrar los mensajes del chat
for i in range(len(messages) - 1, -1, -1):
    with st.chat_message(messages[i]["role"]):
        st.markdown(messages[i]["content"])

# Restantes funciones y código

if 'preguntas' not in st.session_state:
    st.session_state.preguntas = []
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = []

with st.form('my-form'):
    query = st.text_input('¿En qué te puedo ayudar?:', key='user', help='Pulsa Enviar para hacer la pregunta')
    submit_button = st.form_submit_button('Enviar', on_click=click)

if st.session_state.preguntas:
    for i in range(len(st.session_state.respuestas) - 1, -1, -1):
        message(st.session_state.respuestas[i], key=str(i))

    # Opción para continuar la conversación
    continuar_conversacion = st.checkbox('Quieres hacer otra pregunta?')
    if not continuar_conversacion:
        st.session_state.preguntas = []
        st.session_state.respuestas = []
