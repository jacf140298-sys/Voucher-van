import streamlit as st

# Configuración de la página del celular
st.set_page_config(page_title="Mi Control de Vouchers", page_icon="📊", layout="centered")

st.title("📊 Mi Espacio de Control")
st.subheader("Registro de Vouchers - Lunes")

cotilunes = 10

# Estructura lógica del estado de la app (para que no pierda los datos al hacer clic)
if 'lista_vouchers' not in st.session_state:
    st.session_state.lista_vouchers = []

# --- INTERFAZ VISUAL ---
st.info(f"💡 Cotización base de hoy lunes: **${cotilunes}**")

# Formulario para ingresar datos de forma ordenada
with st.form("formulario_voucher", clear_on_submit=True):
    nuevo_monto = st.number_input("Monto del Voucher (S/):", min_value=0.0, step=0.50, value=0.0, format="%0.2f")
    boton_agregar = st.form_submit_button("Agregar Voucher")
    
    if boton_agregar:
        if nuevo_monto > 0:
            st.session_state.lista_vouchers.append(nuevo_monto)
            st.success(f"✅ Voucher de ${nuevo_monto} registrado.")
        else:
            st.warning("El monto debe ser mayor a 0.")

# --- PROCESAMIENTO Y REPORTE ---
if st.session_state.lista_vouchers:
    st.write("### 📝 Vouchers acumulados:")
    
    # Mostramos los elementos en una lista limpia
    for idx, v in enumerate(st.session_state.lista_vouchers, 1):
        st.text(f"• Voucher {idx}: ${v}")
    
    # Cálculos matemáticos exactos
    total_fise_lunes = sum(st.session_state.lista_vouchers)
    total_costo_lunes = cotilunes + total_fise_lunes
    
    st.markdown("---")
    st.write("### 📈 Reporte de Resultados")
    
    # Mostramos los resultados en tarjetas visuales elegantes
    col1, col2 = st.columns(2)
    col1.metric(label="Total FISE Lunes", value=f"${total_fise_lunes}")
    col2.metric(label="Total Costo Lunes", value=f"${total_costo_lunes}")
    
    # Botón para resetear el día
    if st.button("🗑️ Limpiar y empezar nuevo día"):
        st.session_state.lista_vouchers = []
        st.rerun()
else:
    st.write("Aún no hay vouchers registrados para generar el informe.")
