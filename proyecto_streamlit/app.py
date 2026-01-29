import streamlit as st
import streamlit.components.v1 as components
import os
import re

# Configuración de la página
st.set_page_config(layout="wide", page_title="Presentación R&D - Morgan Advanced Materials")

# --- Funciones Auxiliares ---

def natural_sort_key(s):
    """Ordena strings con números de forma humana (1, 2, 10 en vez de 1, 10, 2)."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def load_html_files(directory):
    """Carga lista de archivos HTML ordenados."""
    if not os.path.exists(directory):
        return []
    files = [f for f in os.listdir(directory) if f.endswith(".html")]
    files.sort(key=natural_sort_key)
    return files

# --- Lógica Principal ---

def main():
    st.title("📊 Presentación Interactiva R&D")
    
    # Directorio relativo a este script
    html_dir = "htmls"
    files = load_html_files(html_dir)

    if not files:
        st.error(f"No se encontraron archivos HTML en la carpeta '{html_dir}'.")
        return

    # Gestión del estado (índice de la diapositiva actual)
    if 'slide_index' not in st.session_state:
        st.session_state.slide_index = 0

    # Validar índice (por si cambia el número de archivos)
    if st.session_state.slide_index >= len(files):
        st.session_state.slide_index = 0

    # --- Sidebar de Navegación ---
    with st.sidebar:
        st.header("Navegador")
        
        # Opción 1: Lista seleccionable
        selected_slide = st.radio(
            "Ir a:",
            files,
            index=st.session_state.slide_index,
            key="slide_selector"
        )
        
        # Actualizar índice si se cambia en el sidebar
        if files.index(selected_slide) != st.session_state.slide_index:
            st.session_state.slide_index = files.index(selected_slide)
            st.rerun()

    # --- Botones Superiores ---
    col1, col_mid, col2 = st.columns([1, 8, 1])

    with col1:
        if st.button("⬅️ Anterior", use_container_width=True):
            if st.session_state.slide_index > 0:
                st.session_state.slide_index -= 1
                st.rerun()

    with col2:
        if st.button("Siguiente ➡️", use_container_width=True):
            if st.session_state.slide_index < len(files) - 1:
                st.session_state.slide_index += 1
                st.rerun()

    # --- Visualización ---
    current_file = files[st.session_state.slide_index]
    file_path = os.path.join(html_dir, current_file)

    st.markdown(f"### {current_file} ({st.session_state.slide_index + 1} de {len(files)})")

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Renderizar HTML en un iframe aislado
        # height=850 asegura que quepa la mayoría de gráficas sin doble scroll
        components.html(html_content, height=850, scrolling=True)

    except Exception as e:
        st.error(f"Error cargando archivo: {e}")

if __name__ == "__main__":
    main()
