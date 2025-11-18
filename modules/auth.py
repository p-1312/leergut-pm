import streamlit as st

def login():
    if "user" not in st.session_state:
        st.markdown("<h1 style='text-align:center;'>🍺 Leergut-Profi SLZ 2025</h1>", unsafe_allow_html=True)
        with st.form("login", clear_on_submit=True):
            user = st.text_input("Benutzername")
            pw = st.text_input("Passwort", type="password")
            if st.form_submit_button("Anmelden"):
                if user in ["max", "anna", "tom", "admin"] and pw in ["max123", "anna2025", "tom456", "admin"]:
                    st.session_state.user = user.capitalize()
                    st.success("Erfolgreich angemeldet!")
                    st.rerun()
                else:
                    st.error("Falsche Zugangsdaten")
        st.stop()
    st.sidebar.success(f"Eingeloggt als **{st.session_state.user}**")