import streamlit as st
import random
import matplotlib.pyplot as plt

# Lista de 150 preguntas (solo algunas de ejemplo, puedes añadir más)
questions = [
    "¿Cuál es el color del cielo?",
    "¿Cuántos continentes existen?",
    "¿Cuál es la capital de Francia?",
    "¿Quién escribió 'Cien años de soledad'?",
    "¿Qué es la inteligencia artificial?",
    "¿Cuándo fue la independencia de Venezuela?",
    "¿Qué es un agujero negro?",
    "¿Quién fue el primer presidente de los Estados Unidos?",
    "¿Cuál es el río más largo del mundo?",
    "¿Qué significa la palabra 'tecnología'?"
    # Añadir más preguntas hasta llegar a 150
]

# Función para crear la ruleta
def create_wheel():
    categories = ["Rojo", "Negro", "Verde", "Amarillo", "Azul", "Naranja", "Morado"]
    # Crear un gráfico circular
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie([1] * len(categories), labels=categories, startangle=90, counterclock=False, colors=plt.cm.Paired.colors)
    ax.set_title("Ruleta")
    return fig, categories

# Función para girar la ruleta
def spin_wheel(categories):
    return random.choice(categories)

# Función para obtener una pregunta aleatoria
def get_random_question():
    return random.choice(questions)

# Título de la aplicación
st.title('Ruleta de Colores y Concurso')

# Crear la ruleta
fig, categories = create_wheel()
st.pyplot(fig)

# Girar la ruleta
spin_result = None
if st.button('Girar la ruleta'):
    spin_result = spin_wheel(categories)
    st.subheader(f'La ruleta ha caído en: {spin_result}')

    # Después de que la ruleta se detiene, mostrar la opción de concursar
    if spin_result == "Verde":  # Puedes modificar esta condición para otro color o cualquier otro criterio
        st.success('¡Felicidades! Ahora, tienes la oportunidad de concursar.')

        # Botón para concursar
        if st.button('Concursar'):
            # Mostrar una pregunta aleatoria
            question = get_random_question()
            st.subheader(f'Pregunta: {question}')
            
            # Opción para responder
            user_answer = st.text_input('Tu respuesta:')
            if user_answer:
                st.write(f'¡Gracias por tu respuesta! Tu respuesta fue: {user_answer}')
