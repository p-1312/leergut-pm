import streamlit as st
from modules.auth import login
from modules.katalog import get_katalog, get_lieferanten, get_arten
from modules.auftrag import neue_anmeldung, load_auftraege, save_auftraege

login()

st.title("Leergut-Anmeldung SLZ – Modular & Profi")

tab1, tab2, tab3 = st.tabs(["Neue Anmeldung", "Katalog", "Alle Anmeldungen"])

with tab1:
    st.header("Neue Anmeldung")
    lieferant = st.selectbox("Lieferant", get_lieferanten())
    arten = get_arten(lieferant)
    art = st.selectbox("Leergut-Art", [a["art"] for a in arten])
    selected = next(a for a in arten if a["art"] == art)
    st.image(selected["foto"], width=300)
    menge = st.number_input("Menge", min_value=1)
    beschreibung = st.text_area("Beschreibung")
    if st.button("Anmeldung erstellen"):
        nr = neue_anmeldung(lieferant, art, menge, beschreibung, st.session_state.user)
        st.success(f"Anmeldung {nr} erstellt!")
        st.balloons()

with tab2:
    st.header("Katalog")
    for item in get_katalog():
        col1, col2 = st.columns([1,2])
        with col1:
            st.image(item["foto"], use_column_width=True)
        with col2:
            st.write(f"**{item['art']}** – {item['lieferant']}")
            st.caption(f"Gewicht: {item.get('gewicht_stk', 'k.A.')} kg | Frachtzahler: {item.get('frachtzahler', 'k.A.')}")
            if "sonderregel" in item:
                st.warning(item["sonderregel"])

with tab3:
    st.header("Alle Anmeldungen")
    for auf in load_auftraege():
        status_emoji = {"rot": "🔴", "orange": "🟠", "gelb": "🟡", "grün": "🟢"}
        st.write(f"{status_emoji.get(auf['status'], '⚫')} **{auf['nr']}** – {auf['lieferant']} – {auf['art']} – {auf['menge']} Stk = {auf['gewicht_gesamt']} kg")