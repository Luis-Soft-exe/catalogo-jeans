import streamlit as st

# =========================================
# CONFIGURACIÓN
# =========================================

st.set_page_config(
    page_title="G-Jeans Outlet",
    page_icon="👖",
    layout="centered"
)

# =========================================
# ESTILOS
# =========================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0e1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.modelo {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    border: 1px solid #30363d;
}

.precio {
    color: #00ff99;
    font-size: 28px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITULO
# =========================================

st.title("👖 G-Jeans Outlet")
st.subheader("Catálogo exclusivo")

st.info("""
🔥 Modelos originales y de producción limitada.
""")

# =========================================
# MENU
# =========================================

categoria = st.selectbox(
    "Selecciona categoría",
    ["Inicio", "Caballero", "Dama"]
)

# =========================================
# FUNCIÓN
# =========================================

def mostrar_modelo(nombre, ruta, precio, talla):

    frente = f"{ruta}/frente.jpg"
    trasero = f"{ruta}/trasero.jpg"

    st.markdown(f"""
    <div class="modelo">
        <h3>{nombre}</h3>
        <div class="precio">${precio}</div>
        <p>Talla: {talla}</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image(frente, caption="Frente")

    with col2:
        st.image(trasero, caption="Trasero")

    st.divider()

# =========================================
# CABALLERO
# =========================================

if categoria == "Caballero":

    st.header("🧔 Caballero")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/caballero/modelo_01",
        "799",
        "32"
    )

# =========================================
# DAMA
# =========================================

elif categoria == "Dama":

    st.header("👩 Dama")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/dama/modelo_01",
        "750",
        "28"
    )

# =========================================
# INICIO
# =========================================

else:

    st.markdown("""
    ## Bienvenido 👋

    Selecciona una categoría para comenzar.
    """)
