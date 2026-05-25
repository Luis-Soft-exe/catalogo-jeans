import streamlit as st

# =========================================
# CONFIGURACIÓN
# =========================================

st.set_page_config(
    page_title="Luis.Soft.exe | G-Jeans",
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
    border-radius: 18px;
    margin-bottom: 30px;
    border: 1px solid #30363d;
}

.precio-general {
    background-color: #111827;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #2f3542;
    margin-bottom: 30px;
}

.precio {
    color: #00ff99;
    font-size: 28px;
    font-weight: bold;
}

.texto-suave {
    color: #b8bcc8;
    font-size: 16px;
    line-height: 1.8;
}

.footer {
    text-align: center;
    margin-top: 50px;
    color: #7d8590;
    font-size: 14px;
}

.whatsapp-btn {
    background-color: #25D366;
    color: white;
    padding: 12px 20px;
    border-radius: 10px;
    text-decoration: none;
    font-size: 16px;
    font-weight: bold;
}

</style>
""", unsafe_allow_html=True)

# =========================================
# TITULO PRINCIPAL
# =========================================

st.title("👖 Soft-Jeans-Luis - Premium Collection")

st.subheader("""
Prendas originales de primera calidad • Producción limitada • Piezas únicas
""")

st.info("""
🔥 Cada pieza proviene de excedentes originales de producción.

No manejamos inventario fijo, por lo que muchos modelos pueden no volver a aparecer nuevamente.
""")

# =========================================
# PRECIO GENERAL
# =========================================

st.markdown("""
<div class="precio-general">

<h3>💳 Información General de Venta</h3>

<div class="precio">$500 MXN  de contado y 600 en 2 pagos </div>

<br>

<div class="texto-suave">

✅ Puedes apartar con <b>$300 MXN</b><br><br>

✅ Liquidación restante: <b>$300 MXN</b><br><br>

✅ Tiempo máximo para liquidar: <b>15 días</b>

</div>

</div>
""", unsafe_allow_html=True)

# =========================================
# MENU
# =========================================

categoria = st.selectbox(
    "Selecciona categoría",
    ["Inicio", "Caballero", "Dama"]
)

# =========================================
# FUNCIÓN PARA MOSTRAR MODELOS
# =========================================

def mostrar_modelo(nombre, ruta, talla, largo, corte):

    frente = f"{ruta}/frente.jpg"
    trasero = f"{ruta}/trasero.jpg"

    st.markdown(f"""
    <div class="modelo">

        <h3>{nombre}</h3>

        <p class="texto-suave">

        ✨ Pieza exclusiva disponible<br><br>

        📏 Talla: {talla}<br>

        📐 Largo: {largo}<br>

        👖 Corte: {corte}

        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.image(frente, caption="Vista frontal")

    with col2:
        st.image(trasero, caption="Vista trasera")

    st.divider()

# =========================================
# CABALLERO
# =========================================

if categoria == "Caballero":

    st.header("🧔 Colección Caballero")

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

# =========================================
# DAMA
# =========================================

elif categoria == "Dama":

    st.header("👩 Colección Dama")

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

# =========================================
# INICIO
# =========================================

else:

    st.markdown("""
    ## ✨ Bienvenido a Soft-Jeans-Luis

    Descubre prendas originales de primera calidad.

    Cada modelo es una pieza limitada y exclusiva.
    """)

# =========================================
# WHATSAPP
# =========================================

st.markdown("""
<div style="text-align:center; margin-top:40px;">

<a href="https://wa.me/5217737344018?text=Hola,%20me%20interesa%20un%20modelo%20de%20jeans" target="_blank" class="whatsapp-btn">
📲 Contactar por WhatsApp
</a>

</div>
""", unsafe_allow_html=True)

# =========================================
# FOOTER
# =========================================

st.markdown("""
<div class="footer">

<br><br>

Desarrollado por <b>Luis.Soft.exe</b> 👨‍💻

</div>
""", unsafe_allow_html=True)
