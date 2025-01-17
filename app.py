import streamlit as st


st.logo("./images/irbped_logo.png")


dashboard_page = st.Page(
    "./dashboard.py",
    title="Painel",
    icon="📊",
    default=True
)

sources_page = st.Page(
    "./sources.py",
    title="Créditos",
    icon="ℹ️"
)

pages = {
    "Gráficos": [dashboard_page],
    "Sobre": [sources_page]
}

router = st.navigation(pages)
router.run()