# app_maestro.py
import general
import streamlit as st

page = st.navigation({
    "Dashboards": [
        st.Page(general.show, title="Deserción", icon="📉"),
        # ... otros pages
    ]
})
page.run()