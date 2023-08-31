import streamlit as st
import numpy as np
import pandas as pd
import module_app
from PIL import Image
import requests
import folium


#Import du CSS
module_app.local_css("style.css")


st.title("WEATHER")

    # Titre de l'application

# # Sidebar
# st.sidebar.header("Map")
# Diviser la page en deux colonnes
col1, col2 = st.columns(2)

# Colonne de gauche pour les données météo
with col1:
    # Entrée de la ville
    city_name = st.text_input("Please Enter name of city")

    # Bouton pour envoyer la demande
    if st.button("Send"):
        if city_name:
            module_app.get_weather_data(city_name)
    else:
        st.write("Entrez le nom d'une ville pour afficher les données météo.")


# Colonne de droite pour la carte
with col2:
    st.write("## Carte")
    if city_name:
        # Utilisation de Folium pour afficher la carte
        m = folium.Map(location=[0, 0], zoom_start=2)
        st.write(m)
