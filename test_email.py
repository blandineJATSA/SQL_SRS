import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Utilisateurs et scores
users = {}

# Fonction pour vérifier l'authentification
def authenticate(username, password):
    # Remplacez cette logique par un mécanisme d'authentification sécurisé dans un environnement de production
    return True

# Fonction pour envoyer un e-mail de confirmation
def send_confirmation_email(email, username):
    sender_email = "votre_email@gmail.com"  # Remplacez par votre adresse e-mail
    sender_password = "votre_mot_de_passe"  # Remplacez par votre mot de passe e-mail

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Confirmation de création de compte'

    body = f'Bienvenue, {username}! Votre compte a été créé avec succès.'
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, email, text)
    server.quit()

# Page d'accueil
st.set_page_config(
    page_title="Tutoriel SQL - Exercices",
    page_icon="📚",
    layout="wide"
)

st.title("Tutoriel SQL - Exercices")
sidebar = st.sidebar

# Authentification
sidebar.subheader("Authentification")
username = sidebar.text_input("Nom d'utilisateur:")
password = sidebar.text_input("Mot de passe:", type="password")

# Vérifier si l'utilisateur est déjà enregistré
if username in users:
    if sidebar.button("Connexion"):
        if authenticate(username, password):
            st.success(f"Connexion réussie en tant que {username}!")
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect.")
else:
    email = sidebar.text_input("Adresse e-mail:")
    confirm_password = sidebar.text_input("Confirmer le mot de passe:", type="password")

    if email and password and confirm_password and email not in users.values():
        if password == confirm_password:
            # Enregistrez l'utilisateur
            users[username] = {"email": email, "password": password, "score": 0, "difficult_exercises": []}
            st.success(f"Compte créé avec succès pour {username}! Veuillez vous connecter.")

            # Envoyez un e-mail de confirmation
            send_confirmation_email(email, username)
        else:
            st.error("Les mots de passe ne correspondent pas.")
    elif email in users.values():
        st.error("L'adresse e-mail est déjà utilisée.")
    elif sidebar.button("Créer un compte"):
        st.warning("Veuillez remplir tous les champs.")

# Reste de votre code (affichage des exercices, vérification de la solution, etc.)
