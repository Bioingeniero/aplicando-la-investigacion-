import streamlit as st
import streamlit.components.v1 as components
import os
import re

# Configuración de la página (layout="wide" es vital para ver bien las gráficas)
st.set_page_config(layout="wide", page_title="Presentación R&D")

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

# --- Callbacks para Botones (Solución al problema de que "no funcionan") ---
def ir_siguiente():
    if st.session_state.slide_index < st.session_state.max_index:
        st.session_state.slide_index += 1

def ir_anterior():
    if st.session_state.slide_index > 0:
        st.session_state.slide_index -= 1

def actualizar_desde_slider():
    # El slider devuelve el nombre del archivo, buscamos su índice
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

    # Guardar lista de archivos en session_state para acceso global
    st.session_state.files = files
    st.session_state.max_index = len(files) - 1

    # Inicializar índice
    if 'slide_index' not in st.session_state:
        st.session_state.slide_index = 0

    # --- Sidebar ---
    with st.sidebar:
        st.header("Control de Diapositiva")
        
        # 1. Slider de Navegación (Mejora visual)
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
        
        # 2. Control de Altura (Para solucionar el corte vertical)
        iframe_height = st.slider("Altura del visor (px)", 600, 2000, 1000, 100)
        
        # 3. Control de Ancho (Hack para solucionar el corte horizontal)
        # Esto inyecta CSS en el HTML para escalarlo si es muy ancho
        st.info("Si la diapositiva se ve cortada, reduce la escala.")
        scale_factor = st.slider("Escala (%)", 50, 150, 100, 10) / 100

    # --- Navegación Principal ---
    col1, col_mid, col2 = st.columns([1, 10, 1])

    with col1:
        # on_click ejecuta la función ANTES de recargar la página
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
            
        # Inyectamos CSS para controlar el zoom/escala dentro del iframe
        # Esto ayuda a que el contenido grande quepa en pantallas pequeñas
        if scale_factor != 1.0:
            zoom_css = f"""
            <style>
                body {{
                    transform: scale({scale_factor});
                    transform-origin: 0 0;
                    width: {100/scale_factor}%;
                }}
            </style>
            """
            final_html = zoom_css + raw_html
        else:
            final_html = raw_html

        components.html(final_html, height=iframe_height, scrolling=True)

    except Exception as e:
        st.error(f"Error cargando archivo: {e}")

if __name__ == "__main__":
    main()