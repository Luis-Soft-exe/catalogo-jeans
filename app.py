import streamlit as st

# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="Luis.Soft.exe | G-Jeans",
    page_icon="👖",
    layout="centered"
)

# =====================================
# ESTILOS
# =====================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #0e1117;
    color: white;
}

.modelo {
    background-color: #161b22;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
    border: 1px solid #30363d;
}

.info {
    color: #b8bcc8;
    font-size: 16px;
    line-height: 1.8;
}

.precio-box {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.precio {
    color: #00ff99;
    font-size: 28px;
    font-weight: bold;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: #7d8590;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# TITULO
# =====================================

st.title("👖 Soft-Jeans-Luis Guess-Premium Collection")

st.subheader(
    "Prendas originales • Producción limitada • Piezas únicas"
)

st.info("""
🔥 Cada pieza proviene de excedentes originales de producción.

Muchos modelos pueden no volver a estar disponibles.
""")

# =====================================
# INFORMACIÓN DE VENTA
# =====================================

st.markdown("""
<div class="precio-box">

<h3>💳 Información General</h3>

<div class="precio">$500 MXN Contado y 600 en 2 pagos.</div>

<br>

<div class="info">

✅ Apartando con $300 MXN<br><br>

✅ Restante: $300 MXN<br><br>

✅ Tiempo máximo para liquidar: 8 días

</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# MENU
# =====================================

categoria = st.selectbox(
    "Selecciona categoría",
    ["Inicio", "Caballero", "Dama"]
)

# =====================================
# FUNCIÓN
# =====================================

def mostrar_modelo(nombre, ruta, talla, largo, corte):

    frente = ruta + "/frente.jpg"
    trasero = ruta + "/trasero.jpg"

    st.markdown(
        f"""
        <div class="modelo">

        <h3>{nombre}</h3>

        <div class="info">

        ✨ Pieza exclusiva disponible<br><br>

        📏 Talla: {talla}<br><br>

        📐 Largo: {largo}<br><br>

        👖 Corte: {corte}

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(frente, caption="Vista frontal")

    with col2:
        st.image(trasero, caption="Vista trasera")

    st.divider()

# =====================================
# CABALLERO
# =====================================

if categoria == "Caballero":

    st.header("🔹 Colección Caballero")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/caballero/modelo_01",
        "32",
        "32",
        "Skinny Fit"
    )

    mostrar_modelo(
        "Modelo 02",
        "catalogo/caballero/modelo_02",
        "34",
        "30",
        "Wide Leg"
    )
    mostrar_modelo(
        "Modelo 03",
        "catalogo/caballero/modelo_03",
        "32",
        "32",
        "Regular Fit"
    )

# =====================================
# DAMA
# =====================================

elif categoria == "Dama":

    st.header("✨ Colección Dama")

    mostrar_modelo(
        "Modelo 01",
        "catalogo/dama/modelo_01",
        "28",
        "30",
        "Mom Fit"
    )

    mostrar_modelo(
        "Modelo 02",
        "catalogo/dama/modelo_02",
        "30",
        "32",
        "Straight Fit"
    )

# =====================================
# INICIO
# =====================================

else:

    st.markdown("""
    ## ✨ Bienvenido a Soft-Jeans-Luis

    Descubre prendas originales de primera calidad.

    Cada modelo es una pieza exclusiva.
    """)

# =====================================
# WHATSAPP
# =====================================

st.link_button(
    "📲 Contactar por WhatsApp",
    "https://wa.me/5217737344018?text=Hola,%20me%20interesa%20un%20modelo%20de%20jeans"
)

# =====================================
# FOOTER
# =====================================

st.markdown("""
<div class="footer">

<br><br>

Desarrollado por <b>Luis.Soft.exe</b> 👨‍💻

</div>
""", unsafe_allow_html=True)
