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

        # 1. PARCHE CSS: Sobrescribimos el estilo interno que limita la altura
        css_patch = """
        <style>
            body, html {
                height: auto !important;
                min-height: 100vh !important;
                overflow: visible !important;
            }
            .slide-container {
                height: auto !important;
                min-height: 100vh;
                margin: 0 auto;
            }
        </style>
        """
        
        # Unimos el parche con el HTML original
        html_fixed = css_patch + raw_html
            
        # 2. RENDERIZADO: Usamos una altura FIJA generosa (1100px) 
        # para asegurar que quepa cualquier formato (4:3 o 16:9)
        components.html(html_fixed, height=1100, scrolling=True)

    except Exception as e:
        st.error(f"Error cargando archivo: {e}")

if __name__ == "__main__":
    main()
