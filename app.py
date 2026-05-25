import streamlit as st
import os

# ============================================
# CONFIGURACIÓN PRINCIPAL
# ============================================

st.set_page_config(
    page_title="G-Jeans Outlet",
    page_icon="👖",
    layout="centered"
)

# ============================================
# ESTILOS PERSONALIZADOS
# ============================================

st.markdown("""
<style>

html, body, [class*="css"]  {
    background-color: #0f1117;
    color: white;
}

h1, h2, h3 {
    color: white;
    text-align: center;
}

.stButton>button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    background-color: #1f77ff;
    color: white;
    font-size: 16px;
    border: none;
}

.stSelectbox label {
    color: white !important;
    font-size: 18px;
}

.modelo-box {
    background-color: #161a23;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    border: 1px solid #2b2f3a;
}

.precio {
    font-size: 28px;
    color: #00ff99;
    font-weight: bold;
}

.titulo-modelo {
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 10px;
}

.descripcion {
    color: #b8bcc8;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# ENCABEZADO
# ============================================

st.title("👖 G-Jeans Outlet")
st.subheader("Modelos originales de producción limitada")

st.info("""
🔥 Todas nuestras piezas son originales de exportación.

Cada modelo es único y puede no volver a estar disponible.
""")

# ============================================
# MENÚ PRINCIPAL
# ============================================

categoria = st.selectbox(
    "¿Qué deseas ver?",
    ["Selecciona una opción", "Caballero", "Dama"]
)

# ============================================
# FUNCIÓN PARA MOSTRAR MODELOS
# ============================================

def mostrar_modelo(nombre, ruta, precio, talla):

    frente = f"{ruta}/frente.jpg"
    trasero = f"{ruta}/trasero.jpg"

    st.markdown(f"""
    <div class="modelo-box">
        <div class="titulo-modelo">{nombre}</div>
        <div class="precio">${precio}</div>
        <div class="descripcion">
            Talla disponible: {talla}
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image(frente, caption="Vista frontal")

    with col2:
        st.image(trasero, caption="Vista trasera")

    st.divider()

# ============================================
# SECCIÓN CABALLERO
# ============================================

if categoria == "Caballero":

    st.header("🧔 Sección Caballero")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/caballero/modelo_01",
        "799",
        "32"
    )

    mostrar_modelo(
        "Modelo 02",
        "catalogo/caballero/modelo_02",
        "850",
        "34"
    )

# ============================================
# SECCIÓN DAMA
# ============================================

elif categoria == "Dama":

    st.header("👩 Sección Dama")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/dama/modelo_01",
        "750",
        "28"
    )

    mostrar_modelo(
        "Modelo 02",
        "catalogo/dama/modelo_02",
        "780",
        "30"
    )

# ============================================
# MENSAJE INICIAL
# ============================================

else:

    st.markdown("""
    ## 👖 Bienvenido a G-Jeans Outlet

    Selecciona una categoría para ver los modelos disponibles.
    """)
