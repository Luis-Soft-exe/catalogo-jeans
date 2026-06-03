import streamlit as st
import os

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
# TÍTULO
# =====================================

st.title("👖 LuisSx-Jeans Premium Collection")

st.subheader("Prendas originales • Producción limitada • Piezas únicas")

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

<div class="precio">$550 MXN Contado y $650 MXN en 2 pagos</div>

<br>

<div class="info">

✅ Apartando con $300 MXN<br><br>

✅ Restante: $350 MXN<br><br>

✅ Tiempo máximo para liquidar: 8 días

</div>

</div>
""", unsafe_allow_html=True)

# =====================================
# MENÚ
# =====================================

categoria = st.selectbox(
    "Selecciona categoría",
    ["Inicio", "Caballero", "Dama"]
)

# =====================================
# FUNCIÓN MODELO
# =====================================

def mostrar_modelo(
    nombre,
    ruta,
    marca,
    tono,
    talla,
    largo,
    corte,
    disponible
):

    frente = ruta + "/frente.jpg"
    trasero = ruta + "/trasero.jpg"

    estado = "🟢 Disponible" if disponible else "🔴 Vendido"

    st.markdown(
        f"""
        <div class="modelo">

        <h3>{nombre}</h3>

        <div class="info">

        🏷️ Marca: {marca}<br><br>

        🎨 Tono: {tono}<br><br>

        📏 Talla: {talla}<br><br>

        📐 Largo: {largo}<br><br>

        👖 Corte: {corte}<br><br>

        {estado}

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        st.image(frente, caption="Vista frontal", use_container_width=True)

    with col2:
        st.image(trasero, caption="Vista trasera", use_container_width=True)

    mensaje = (
        f"Hola, me interesa el modelo {nombre}. "
        f"Marca: {marca}. "
        f"Tono: {tono}. "
        f"Talla: {talla}. "
        f"Largo: {largo}. "
        f"Corte: {corte}. "
        f"¿Sigue disponible?"
    )

    mensaje_url = mensaje.replace(" ", "%20")

    st.link_button(
        f"📲 Preguntar por {nombre}",
        f"https://wa.me/5217737344018?text={mensaje_url}"
    )

    st.divider()

# =====================================
# CABALLERO (AUTOMÁTICO)
# =====================================

if categoria == "Caballero":

    st.header("🔹 Colección Caballero")

    base = "catalogo/caballero"
    i = 1

    while True:
        ruta = f"{base}/modelo_{str(i).zfill(2)}"

        if not os.path.exists(ruta):
            break

        mostrar_modelo(
            f"Modelo Caballero {i}",
            ruta,
            "GUESS",
            "N/D",
            "N/D",
            "N/D",
            "N/D",
            True
        )

        i += 1

# =====================================
# DAMA (AUTOMÁTICO)
# =====================================

elif categoria == "Dama":

    st.header("✨ Colección Dama")

    base = "catalogo/dama"
    i = 1

    while True:
        ruta = f"{base}/modelo_{str(i).zfill(2)}"

        if not os.path.exists(ruta):
            break

        mostrar_modelo(
            f"Modelo Dama {i}",
            ruta,
            "GUESS",
            "N/D",
            "N/D",
            "N/D",
            "N/D",
            True
        )

        i += 1

# =====================================
# INICIO
# =====================================

else:

    st.markdown("""
    ## ✨ Bienvenido a LuisSx Jeans-Premium Collection

    Descubre prendas originales de excelente calidad.

    Piezas seleccionadas provenientes de excedentes originales de producción.

    Cada modelo es único y la disponibilidad cambia constantemente.
    """)

# =====================================
# FOOTER
# =====================================

st.markdown("""
<div class="footer">

<br><br>

Desarrollado por <b>Luis.Soft.exe</b> 👨‍💻

</div>
""", unsafe_allow_html=True)
