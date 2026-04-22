# # app_maestro.py
# import general
# import streamlit as st

# page = st.navigation({
#     "Dashboards": [
#         st.Page(general.show, title="Deserción", icon="📉"),
#         # ... otros pages
#     ]
# })
# page.run()

"""
app_maestro.py
Archivo principal de la aplicación Streamlit.
Gestiona la navegación entre dashboards desde el menú lateral.
"""

import streamlit as st

# ─────────────────────────────────────────────
#  CONFIGURACIÓN DE PÁGINA (debe ir primero)
# ─────────────────────────────────────────────

st.set_page_config(
    page_title="Sistema de Analítica Académica",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  IMPORTAR PÁGINAS / DASHBOARDS
# ─────────────────────────────────────────────
# Para agregar un nuevo dashboard:
#   1. Crea el archivo (ej: rendimiento_dashboard.py) con una función show()
#   2. Impórtalo aquí
#   3. Agrégalo al diccionario PAGES

import general as general_dashboard
# import rendimiento_dashboard   # ← descomenta al agregar más dashboards
# import pagos_dashboard
# import engagement_dashboard


# ─────────────────────────────────────────────
#  ESTILOS GLOBALES
# ─────────────────────────────────────────────

st.markdown("""
<style>
    /* Fondo general */
    [data-testid="stAppViewContainer"] {
        background-color: #0F0F1A;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1A2E 0%, #16213E 100%);
        border-right: 1px solid #2a2a4a;
    }

    /* Ocultar decoración por defecto de Streamlit */
    #MainMenu, footer, header { visibility: hidden; }

    /* Botones del menú lateral */
    div[data-testid="stSidebar"] button {
        width: 100%;
        border-radius: 10px;
        border: none;
        padding: 10px 16px;
        text-align: left;
        font-size: 0.92rem;
        font-weight: 500;
        transition: background 0.2s;
        margin-bottom: 4px;
    }

    /* Radio buttons como nav */
    div[data-testid="stSidebar"] .stRadio > label {
        color: #aab4be !important;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  DEFINICIÓN DEL MENÚ
# ─────────────────────────────────────────────

# Estructura: { "Categoría": [(icono, nombre_display, módulo)] }
MENU = {
    "📊 Analítica Estudiantil": [
        ("📉", "Deserción Estudiantil",  general_dashboard),
        # ("📈", "Rendimiento Académico", rendimiento_dashboard),
    ],
    # "💳 Gestión Financiera": [
    #     ("💰", "Pagos y Morosidad",     pagos_dashboard),
    # ],
    # "💻 Plataforma LMS": [
    #     ("🖥️", "Engagement Digital",   engagement_dashboard),
    # ],
}

# Página de inicio por defecto
HOME_KEY = "🏠  Inicio"


# ─────────────────────────────────────────────
#  ESTADO DE SESIÓN — página activa
# ─────────────────────────────────────────────

if "active_page" not in st.session_state:
    st.session_state.active_page = HOME_KEY


# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────

with st.sidebar:

    # — Logo / título del sistema —
    st.markdown("""
    <div style="padding:16px 8px 20px 8px; text-align:center;">
        <div style="font-size:2.4rem;">🎓</div>
        <div style="font-size:1rem; font-weight:700; color:#EAEAEA;
                    letter-spacing:0.03em; line-height:1.3;">
            Analítica<br>Académica
        </div>
        <div style="font-size:0.72rem; color:#6a7280; margin-top:4px;">
            Ingeniería de Software
        </div>
    </div>
    <hr style="border-color:#2a2a4a; margin:0 0 16px 0;">
    """, unsafe_allow_html=True)

    # — Botón Inicio —
    is_home = st.session_state.active_page == HOME_KEY
    home_style = (
        "background:#1e3a5f; color:#63b3ed; border:1px solid #2b6cb0;"
        if is_home else
        "background:transparent; color:#cbd5e0; border:1px solid transparent;"
    )
    if st.button(
        HOME_KEY,
        key="nav_home",
        use_container_width=True,
        help="Ir a la pantalla de inicio",
    ):
        st.session_state.active_page = HOME_KEY
        st.rerun()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # — Categorías y dashboards —
    for category, pages in MENU.items():
        st.markdown(
            f"<div style='font-size:0.7rem; color:#4a5568; text-transform:uppercase;"
            f"letter-spacing:0.1em; padding:10px 4px 4px 4px;'>{category}</div>",
            unsafe_allow_html=True,
        )
        for icon, label, _ in pages:
            full_label = f"{icon}  {label}"
            is_active  = st.session_state.active_page == full_label
            btn_type   = "primary" if is_active else "secondary"

            if st.button(
                full_label,
                key=f"nav_{label}",
                use_container_width=True,
                type=btn_type,
            ):
                st.session_state.active_page = full_label
                st.rerun()

    # — Footer del sidebar —
    st.markdown("""
    <hr style="border-color:#2a2a4a; margin-top:auto;">
    <div style="font-size:0.7rem; color:#4a5568; text-align:center; padding:8px 0;">
        v1.0.0 · Streamlit + MongoDB<br>
        <span style="color:#2a2a4a;">──────────────</span>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
#  ENRUTADOR — renderiza la página activa
# ─────────────────────────────────────────────

active = st.session_state.active_page

# Construir mapa plano: full_label → módulo
PAGE_MAP = {}
for pages in MENU.values():
    for icon, label, module in pages:
        PAGE_MAP[f"{icon}  {label}"] = module

if active == HOME_KEY:

    # ── Pantalla de inicio ──────────────────
    st.markdown("""
    <div style="background:linear-gradient(135deg,#1A1A2E 0%,#16213E 60%,#0F3460 100%);
                border-radius:16px; padding:40px 48px; margin-bottom:32px;
                border:1px solid #2a2a4a;">
        <h1 style="color:#EAEAEA; font-size:2.2rem; margin:0 0 8px 0;">
            👋 Bienvenido al Sistema de Analítica
        </h1>
        <p style="color:#8892a4; font-size:1rem; margin:0;">
            Selecciona un dashboard en el menú lateral para comenzar.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # — Tarjetas de acceso rápido —
    st.markdown(
        "<h3 style='color:#EAEAEA; font-size:1rem; margin-bottom:16px;'>"
        "🚀 Acceso Rápido</h3>",
        unsafe_allow_html=True,
    )

    all_pages = [(icon, label, mod) for pages in MENU.values() for icon, label, mod in pages]
    cols = st.columns(min(len(all_pages), 3))

    CARD_DESCRIPTIONS = {
        "Deserción Estudiantil": (
            "Monitorea tasas de deserción, motivos académicos y financieros, "
            "alertas tempranas y engagement en el LMS.",
            "#E63946",
        ),
        # "Rendimiento Académico": ("Análisis de notas, aprobación por curso y tendencias.", "#457B9D"),
        # "Pagos y Morosidad":     ("Estado de pagos, deudas pendientes y morosidad.", "#F4A261"),
        # "Engagement Digital":    ("Actividad en plataformas LMS y participación.", "#2A9D8F"),
    }

    for col, (icon, label, _) in zip(cols, all_pages):
        desc, color = CARD_DESCRIPTIONS.get(label, ("Dashboard disponible.", "#457B9D"))
        full_label  = f"{icon}  {label}"
        with col:
            st.markdown(f"""
            <div style="background:linear-gradient(135deg,#16213E,#1a2744);
                        border-radius:12px; padding:24px; border-top:3px solid {color};
                        border:1px solid #2a2a4a; height:180px;">
                <div style="font-size:2rem; margin-bottom:8px;">{icon}</div>
                <div style="font-size:1rem; font-weight:600; color:#EAEAEA;
                            margin-bottom:8px;">{label}</div>
                <div style="font-size:0.82rem; color:#8892a4; line-height:1.5;">
                    {desc}
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

            if st.button(f"Abrir →", key=f"home_btn_{label}", use_container_width=True):
                st.session_state.active_page = full_label
                st.rerun()

    # — Estadísticas del sistema —
    st.markdown("<div style='height:24px'></div>", unsafe_allow_html=True)
    st.markdown(
        "<h3 style='color:#EAEAEA; font-size:1rem; margin-bottom:12px;'>"
        "📋 Módulos Disponibles</h3>",
        unsafe_allow_html=True,
    )

    total_dashboards = sum(len(p) for p in MENU.values())
    total_categorias = len(MENU)

    i1, i2, i3 = st.columns(3)
    with i1:
        st.metric("Dashboards activos",  total_dashboards)
    with i2:
        st.metric("Categorías",          total_categorias)
    with i3:
        st.metric("Fuente de datos",     "MongoDB Atlas")

elif active in PAGE_MAP:
    # ── Renderizar dashboard seleccionado ───
    PAGE_MAP[active].show()

else:
    st.error(f"Página '{active}' no encontrada.")
    if st.button("← Volver al inicio"):
        st.session_state.active_page = HOME_KEY
        st.rerun()