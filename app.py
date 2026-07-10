import streamlit as st
import os

# =====================================
# CONFIGURACIÓN
# =====================================

st.set_page_config(
    page_title="Sx.exe | Sx-Jeans Premium Collection",
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

st.title("👖 Jeans Sx-Premium Collection")

st.subheader("Prendas originales • Producción limitada • Piezas únicas")

# =====================================
# INFO
# =====================================

st.info("""
✨ Catálogo de prendas originales en cantidades limitadas.

La disponibilidad puede cambiar en cualquier momento.

El estado de cada modelo indica si está disponible o vendido.

También puedes usar el catálogo como referencia para que pueda conseguirte modelos similares o de ese estilo.
""")

# =====================================
# PRECIO (CORREGIDO)
# =====================================

st.markdown("""
<div class="precio-box">

<h3> Selecciona la categoría de tu interés:</h3>

<div style="color:#00ff99; font-size:28px; font-weight:bold; margin:10px 0;">

</div>

<div class="info">

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

    st.markdown(f"""
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
    """, unsafe_allow_html=True)

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
# CABALLERO
# =====================================

if categoria == "Caballero":

    st.header("🔹 Colección Caballero")

    base = "catalogo/caballero"

    info_caballero = {
        1: ("Guess Black Regular Straight", "Negro", "36", "32", "Regular Straight"),
        2: ("Guess Regular Straight Hason", "Medio", "32", "32", "Regular Straight"),
        3: ("Guess Slim Straight", "Negro", "33", "32", "Slim Straight"),
        4: ("Guess Slim Tapered", "Claro", "34", "32", "Slim Tapered"),
        5: ("Guess Regular Straight", "Medio", "32", "32", "Regular Straight"),
        6: ("Guess Slim Tapered", "Medio", "36", "32", "Slim Tapered"),
        7: ("Guess Slim Straight", "Medio", "34", "32", "Slim Straight"),
        8: ("Guess Slim Straight", "Entintado Cafe ", "32", "32", "Slim Straight")
    }

    vendidos_caballero = [2, 3, 4]

    i = 1

    while True:
        ruta = f"{base}/modelo_{str(i).zfill(2)}"

        if not os.path.exists(ruta):
            break

        nombre, tono, talla, largo, corte = info_caballero.get(
            i, ("N/D", "N/D", "N/D", "N/D", "N/D")
        )

        disponible = i not in vendidos_caballero

        mostrar_modelo(
            nombre,
            ruta,
            "GUESS",
            tono,
            talla,
            largo,
            corte,
            disponible
        )

        i += 1

# =====================================
# DAMA
# =====================================

elif categoria == "Dama":

    st.header("✨ Colección Dama")

    base = "catalogo/dama"

    info_dama = {
        1: ("Guess Sexy Boot Medium Wash", "Medio", "28", "30", "Sexy Boot"),
        2: ("Guess 1981 Skinny Light Wash", "Claro", "27", "30", "Skinny"),
        3: ("Guess Mom Low Rise Slouchy", "Medio", "28", "30", "Mom Slouchy"),
        4: ("Guess Low Rise Slouchy", "Medio", "29", "30", "Low Rise Slouchy"),
        5: ("Guess Sexy Boot", "Oscuro", "25", "30", "Sexy Boot"),
        6: ("Guess Sexy Boot", "Claro", "26", "30", "Sexy Boot"),
        7: ("Guess 1981 Skinny ", "Medio", "24", "30", "Skinny"),
        8: ("Guess Low Rise Slouchy", "Medio", "26", "30", "Low Rise Slouchy"),
        9: ("Guess Sexy Boot", "Medio", "26", "30", "Sexy Boot"),
        10: ("Guess Power Curvy Mid", "Claro", "30", "30", "Power Curvy Mid"),
        11: ("Guess Higt Rise Flare", "Claro", "28", "30", "Higt Rise Flare"),
        12: ("Guess Higt Rise Flare", "Medio", "28", "30", "Higt Rise Flare")
    }

    vendidos_dama = [3]

    i = 1

    while True:
        ruta = f"{base}/modelo_{str(i).zfill(2)}"

        if not os.path.exists(ruta):
            break

        nombre, tono, talla, largo, corte = info_dama.get(
            i, ("N/D", "N/D", "N/D", "N/D", "N/D")
        )

        disponible = i not in vendidos_dama

        mostrar_modelo(
            nombre,
            ruta,
            "GUESS",
            tono,
            talla,
            largo,
            corte,
            disponible
        )

        i += 1

# =====================================
# INICIO
# =====================================

else:

    st.markdown("""
    ## ✨ Bienvenido a Sx Jeans-Premium Collection

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
