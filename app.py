import streamlit as st
import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Lista de opciones
options = ["Opción 1", "Opción 2", "Opción 3", "Opción 4", "Opción 5", "Opción 6", "Opción 7"]

# Función para crear la ruleta
def create_wheel():
    # Crear los colores de la ruleta
    colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#F1C40F', '#9B59B6', '#1ABC9C']

    # Ángulos de cada sección
    angles = np.linspace(0, 2 * np.pi, len(options), endpoint=False)
    
    # Crear un gráfico circular
    fig, ax = plt.subplots(figsize=(6, 6))
    wedges, texts = ax.pie([1] * len(options), labels=options, startangle=90, counterclock=False, colors=colors, wedgeprops={'edgecolor': 'black'})

    ax.set_title("Ruleta de Opciones")
    return fig, ax, wedges

# Función para girar la ruleta
def spin_wheel():
    return random.choice(options)

# Función para animar la ruleta
def animate_wheel(ax, wedges, options, spins=10):
    def update(frame):
        ax.clear()
        # Girar la ruleta
        angle = frame * (360 / len(options))
        fig, ax, wedges = create_wheel()
        ax.set_title("Ruleta de Opciones")
        return wedges,
    
    ani = FuncAnimation(fig, update, frames=np.arange(0, spins), interval=100, blit=True)
    return ani

# Título de la aplicación
st.title('Ruleta Interactiva')

# Crear la ruleta
fig, ax, wedges = create_wheel()
st.pyplot(fig)

# Girar la ruleta
if st.button('Girar la ruleta'):
    spin_result = spin_wheel()
    st.subheader(f'La ruleta ha caído en: {spin_result}')

    # Mostrar la animación de giro
    ani = animate_wheel(ax, wedges, options, spins=30)
    st.pyplot(fig)
