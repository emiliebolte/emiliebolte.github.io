import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd

df_authentificator = pd.read_csv('users.csv', sep=";")

# On transforme le CSV en dictionnaire indexé par 'username'
users_dict = df_authentificator.set_index('name', drop=False).to_dict('index')
# On l'insère dans la structure attendue
credentials = {'usernames': users_dict}
# Puis on initialise
authenticator = Authenticate(credentials, "cookie_name", "cookie_key", 30)
authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page")
      st.image("https://www.lovstickers.com/14877-large_default/stickers-calligraphie-welcome-modele-no-05.jpg")

if st.session_state["authentication_status"]:
  # Le bouton de déconnexion
    authenticator.logout("Déconnexion", "sidebar")
    nom_utilisateur = st.session_state["name"]
    with st.sidebar: 
        st.write(f"### Bienvenue {nom_utilisateur} !")
        selection = option_menu(menu_title=None, options=["🤩Accueil", "😻 Photos de mes chats"])
    
    if selection == "🤩Accueil":
            accueil()
    elif selection == "😻 Photos de mes chats":
        st.title ("Les photos de mes chats")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.header("Vindhya")
            st.image("images/Vindhya.jpg")
        with col2:
            st.header("Nyaeve")
            st.image("images/Nyaeve.jpg")
        with col3:
            st.header("Mushu")
            st.image("images/Mushu.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')
    st.write("Utilisez root/rootMDP ou Emilie/emilie pour vous connecter")