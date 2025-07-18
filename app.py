import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.title("Calculadora de Derivadas con Visualización")

# Entrada de la función
st.subheader("Ingresa una función de una variable (por ejemplo: sin(x), x**2, exp(x))")
func_input = st.text_input("f(x) =", value="x**2")

# Definimos la variable simbólica
x = sp.Symbol('x')

try:
    # Parsear y derivar la función
    func = sp.sympify(func_input)
    deriv = sp.diff(func, x)

    st.latex(f"f(x) = {sp.latex(func)}")
    st.latex(f"f'(x) = {sp.latex(deriv)}")

    # Mostrar gráfico si se activa la opción
    if st.checkbox("Mostrar gráfico de f(x) y su derivada f'(x)"):
        # Crear función numérica para graficar
        f_lambd = sp.lambdify(x, func, modules=["numpy"])
        d_lambd = sp.lambdify(x, deriv, modules=["numpy"])

        # Rango de valores para graficar
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_lambd(x_vals)
        dy_vals = d_lambd(x_vals)

        # Gráfico
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='f(x)', color='blue')
        ax.plot(x_vals, dy_vals, label="f'(x)", color='red', linestyle='--')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.legend()
        ax.set_title("Función y su Derivada")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        st.pyplot(fig)

except Exception as e:
    st.error(f"Ocurrió un error al procesar la función: {e}")
