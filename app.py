import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd





def setup():
    users_csv = pd.read_csv("users.csv", sep=",")
    users_data = {'usernames': dict()}
    for row in users_csv.iterrows():
        username = row[1]['username']
        row_to_dict = row[1].to_dict()
        users_data['usernames'][username] = row_to_dict 

    authenticator = Authenticate(
        users_data, # Les données des comptes
        "cookie name", # Le nom du cookie, un str quelconque
        "cookie key", # La clé du cookie, un str quelconque
        30, # Le nombre de jours avant que le cookie expire 
    )
    return authenticator


def welcome_page():
    st.title("Bienvenue sur le site")
    st.image("https://doodleipsum.com/700/flat?i=9893ff3c320fea0230c7597d898380d2")
    
def animals_images_page():
    st.title("Say hello to my little friends")
    col1, col2, col3 = st.columns(3)

    with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")
    


def main():
    authenticator = setup()
    authenticator.login()
    if st.session_state["authentication_status"]:
        
        # side bar
  
        username = st.session_state["username"]
        
        #
        #st.sidebar.title(f"Welcome to the site {username}")
        # add option menu to the sidebar
        #sidebar.
        
        with st.sidebar:
            st.title(f"Welcome to the site {username}")
            selection = option_menu(
                menu_title=None,
                options = ["Home Page", "Pictures of animals"],
            )
            authenticator.logout("logout")
        if selection == "Home Page":
            welcome_page()
        elif selection == "Pictures of animals":
            animals_images_page()
        
    # Le bouton de déconnexion   
    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning('Les champs username et mot de passe doivent être remplie') 

  

    
if __name__ == "__main__":
    main()