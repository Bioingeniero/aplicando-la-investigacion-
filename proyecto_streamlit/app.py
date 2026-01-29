import streamlit as st
import streamlit.components.v1 as components
import os
import re

# Configuración de la página (layout="wide" es vital para ver bien las gráficas)
st.set_page_config(layout="wide", page_title="Presentación R&D")

# --- CSS Global para Streamlit (eliminar borde del iframe) ---
# Esto afectará a todos los iframes de Streamlit en la página.
st.markdown("""
<style>
    iframe {
        border: none !important; /* Elimina el borde del iframe */
    }
</style>
""", unsafe_allow_html=True)


# --- Funciones Auxiliares ---

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def load_html_files(directory):
    if not os.path.exists(directory):
        return []
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    files.sort(key=natural_sort_key)
    return files

# --- Callbacks para Botones ---
def ir_siguiente():
    if st.session_state.slide_index < st.session_state.max_index:
        st.session_state.slide_index += 1

def ir_anterior():
    if st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1

def actualizar_desde_slider():
    files = st.session_state.files
    selection = st.session_state.slider_selection
    if selection in files:
        st.session_state.slide_index = files.index(selection)

# --- App Principal ---

def main():
    st.title("📊 Presentación Interactiva R&D")
    
    html_dir = "htmls"
    files = load_html_files(html_dir)
    
    if not files:
        st.error("No se encontraron archivos HTML.")
        return

    st.session_state.files = files
    st.session_state.max_index = len(files) - 1

    if 'slide_index' not in st.session_state:
        st.session_state.slide_index = 0

    if st.session_state.slide_index >= len(files):
        st.session_state.slide_index = 0

    # --- Sidebar ---
    with st.sidebar:
        st.header("Control de Diapositiva")
        
        current_file = files[st.session_state.slide_index]
        st.select_slider(
            "Desliza para cambiar:",
            options=files,
            value=current_file,
            key="slider_selection",
            on_change=actualizar_desde_slider
        )
        
        st.markdown("---")
        st.header("Ajustes de Visualización")
        
        iframe_height = st.slider("Altura del visor (px)", 600, 2000, 1200, 100)
        
        st.info("Si la diapositiva se ve cortada, reduce la escala.")
        scale_factor = st.slider("Escala (%)", 50, 150, 85, 5) / 100

    # --- Navegación Principal ---
    col1, col_mid, col2 = st.columns([1, 10, 1])

    with col1:
        st.button("⬅️ Anterior", on_click=ir_anterior, use_container_width=True)

    with col2:
        st.button("Siguiente ➡️", on_click=ir_siguiente, use_container_width=True)

    # --- Renderizado ---
    current_file_name = files[st.session_state.slide_index]
    file_path = os.path.join(html_dir, current_file_name)

    st.caption(f"Visualizando: `{current_file_name}` ({st.session_state.slide_index + 1}/{len(files)})")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_html = f.read()
            
        # CSS a inyectar en el HTML para corregir el layout fijo de las diapositivas
        # 1. Ajustamos el body para permitir scroll si es necesario, pero centrar contenido
        # 2. Atacamos específicamente a .slide-container (que tiene width: 1280px fijo)
        #    para escalarlo y que quepa en el iframe.
        injection_css = f"""
        <style>
            body {{
                margin: 0 !important;
                padding: 0 !important;
                background-color: #121212 !important; /* Coincidir con el fondo de las diapos */
                display: flex !important;
                justify-content: center !important;
                align-items: flex-start !important; /* Alineamos arriba para que el scale no corte la cabecera */
                min-height: 100vh !important;
                overflow: auto !important; /* Permitir scroll si el zoom es muy grande */
            }}
            
            /* Corrección específica para tus diapositivas (6, 11, 12, etc.) */
            .slide-container {{
                transform: scale({scale_factor});
                transform-origin: top center; /* Escalar desde arriba centro */
                margin-top: 20px !important;
                margin-bottom: 20px !important;
                box-shadow: 0 0 20px rgba(0,0,0,0.5) !important; /* Resaltar el borde para ver los límites */
            }}

            /* Para diapositivas que no usen .slide-container, aplicamos un fallback genérico */
            body > div:first-child:not(.slide-container) {{
                transform: scale({scale_factor});
                transform-origin: top center;
            }}
        </style>
        """
        
        # Inyectamos el CSS justo después del <head> o al inicio del <body>
        # Buscamos la etiqueta de cierre de <head> o inicio de <body> para la inyección
        if "<head>" in raw_html:
            final_html = raw_html.replace("<head>", "<head>" + injection_css)
        elif "<body>" in raw_html:
            final_html = raw_html.replace("<body>", "<body>" + injection_css)
        else: # Si no hay head ni body (poco común pero posible en fragmentos HTML)
            final_html = injection_css + raw_html


        components.html(final_html, height=iframe_height, scrolling=True)

    except Exception as e:
        st.error(f"Error cargando archivo: {e}")

if __name__ == "__main__":
    main()
