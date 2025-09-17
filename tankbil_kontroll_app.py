# Streamlit app for tankbilkontroll laget for Bjørnar Buskum

import streamlit as st
import pandas as pd
from datetime import datetime

# Tittel
st.title("Tankbil Kontroll App")

# Seksjon: Grunnleggende informasjon
st.header("Grunnleggende informasjon")
dato = st.date_input("Dato for kontroll", value=datetime.today())
kontrollør = st.text_input("Navn på kontrollør")
tankbil_id = st.text_input("Tankbil ID / Registreringsnummer")

# Seksjon: Visuell inspeksjon
st.header("Visuell inspeksjon")
visuell_ok = st.radio("Er det synlige skader på tanken?", ["Nei", "Ja"])
skadebeskrivelse = ""
if visuell_ok == "Ja":
    skadebeskrivelse = st.text_area("Beskriv skaden")

# Seksjon: Trykktest
st.header("Trykktest")
trykktest_ok = st.radio("Bestått trykktest?", ["Ja", "Nei"])
trykkverdi = st.number_input("Registrert trykkverdi (bar)", min_value=0.0, step=0.1)

# Seksjon: Ventiler og koblinger
st.header("Ventiler og koblinger")
ventiler_ok = st.checkbox("Alle ventiler fungerer som de skal")
koblinger_ok = st.checkbox("Alle koblinger er tette")

# Seksjon: Kommentarer og signatur
st.header("Kommentarer og signatur")
kommentarer = st.text_area("Andre kommentarer")
signatur = st.text_input("Signatur (navn)")

# Lagre data
if st.button("Lagre kontrollrapport"):
    rapport = {
        "Dato": dato,
        "Kontrollør": kontrollør,
        "Tankbil ID": tankbil_id,
        "Visuell skade": visuell_ok,
        "Skadebeskrivelse": skadebeskrivelse,
        "Trykktest bestått": trykktest_ok,
        "Trykkverdi (bar)": trykkverdi,
        "Ventiler OK": ventiler_ok,
        "Koblinger OK": koblinger_ok,
        "Kommentarer": kommentarer,
        "Signatur": signatur
    }

    df = pd.DataFrame([rapport])
    filnavn = f"kontrollrapport_{tankbil_id}_{dato}.xlsx"
    df.to_excel(filnavn, index=False)
    st.success(f"Kontrollrapport lagret som {filnavn}")
