import pandas as pd
import streamlit as st
import duckdb as db
import pandas as pd
# Page d'accueil
st.set_page_config(
    page_title="Tutoriel SQL - Exercices",
    page_icon="📚",
    layout="wide"
)

# Définissez la couleur de fond
st.markdown(
    """
    <style>
        body {
            background-color: #f4f4f4;
        }
    </style>
    """,
    unsafe_allow_html=True
)

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)

st.title("Projet  SQL Tutorial ")

# st.write("Ce project propose des exercices interactifs pour apprendre et pratiquer SQL.")
# st.header("Bienvenue dans le projet SQL réalisé par Blandine JATSA NGUETSE.")
# st.markdown("**Bienvenue dans notre projet interactif SQL !**")

# Zone de texte pour la solution de l'utilisateur
sql_query = st.text_area("Votre solution SQL :")
result = db.query(sql_query).df()
st.write(f"vous avez entré le query suivant : {sql_query}")
st.dataframe(result)

sidebar = st.sidebar

# Authentification
sidebar.subheader("Authentification")
