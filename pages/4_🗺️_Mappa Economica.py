###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
import datetime as dt
from dateutil.relativedelta import relativedelta
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import string
import math


css_prova="""
<style>
[data-testid="stImage"]{
    padding-left: 40%;
    padding-right: 40%;
}

[data-testid="stAppViewContainer"]{
    background-image: url(https://images5.alphacoders.com/129/1297020.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="mappa-economica"]{
    font-size: 72px;
    color: crimson;
    text-shadow: -1px 0 snow, 0 1px snow, 1px 0 snow, 0 -1px snow;
}

[data-testid="stSidebar"]{
    background-color: #09a1fc;
    opacity: 0.9;
}
[data-testid="stHeader"]{
    background-color: black;
}
[data-testid="stToolbar"]{
    color: white;
}
[data-testid="stMarkdownContainer"]{
    
    width: 1655px !important; 
   
}
[data-testid="collapsedControl"]{
    color: white;
   
}

td{
    padding: 0px 0px 0px 0px !important;
    color: darkblue !important;
}
tr{
    padding: 0px 0px 0px 0px !important;
    text-align: left !important;
    font-size: 14px !important;
    color: darkblue !important;
}
tbody{
    padding: 0px 0px 0px 0px !important;
}
th{
    padding: 0px 0px 0px 0px !important;
}
.css-1hverof:visited{
    color:black;
}
.css-17lntkn{
    color:black;
}
.css-17nby6i:visited{
    background-color: rgb(255 255 255) !important
}
.css-nziaof:active, .css-nziaof:visited{
    background: black;

}

h2{
    color: limegreen;
    font-weight: bold !important;
}
.main-svg{
    border-radius: 100px;
    border-style: solid;
    border-color: #1b96ff;
    border-width: 5px;
    padding: 20px ;
}






</style>

"""



###Informazioni Pagina
st.set_page_config(
    page_title="Bandi",
    page_icon="📑",
    layout="wide"
)



st.title("Mappa Economica 🗺️")



###Lettura Dataset
local_filename = 'Dataset_Bandi.xlsx'

dati = pd.read_excel(local_filename)



dati_Filtered2 = dati.groupby(["Funder Country"]).agg({"Funding Amount in EUR": "sum"}).reset_index()


# crea una nuova colonna contenente le coordinate geografiche dei paesi
geolocator = Nominatim(user_agent="my_app", timeout=5)


def get_lat_long(country):
    try:
        location = geolocator.geocode(country)
        return location.latitude, location.longitude
    except:
        return None, None

dati_Filtered2[["lat", "long"]] = dati_Filtered2["Funder Country"].apply(lambda x: pd.Series(get_lat_long(x)))



# impostiamo il valore minimo per la dimensione dei punti
size_min = 2

# calcoliamo il valore minimo dei "Funding Amount in EUR"
funding_min = dati_Filtered2["Funding Amount in EUR"].min()

# calcoliamo la dimensione dei punti, mappando i valori inferiori al valore minimo
dati_Filtered2["size"] = np.clip(dati_Filtered2["Funding Amount in EUR"], funding_min, None)
dati_Filtered2["size"] = (dati_Filtered2["size"] - funding_min) / (dati_Filtered2["Funding Amount in EUR"].max() - funding_min)
dati_Filtered2["size"] = dati_Filtered2["size"] * (80 - size_min) + size_min

# Creiamo lo scatter plot geografico
fig = px.scatter_geo(dati_Filtered2, 
                     lat="lat", 
                     lon="long", 
                     size="size", 
                     color="Funder Country",
                     hover_name="Funder Country",
                     projection="natural earth",
                     size_max=80,
                     width=2000,
                     height=1200)

# Mostraimo il grafico su Streamlit
st.plotly_chart(fig, use_container_width=True)

st.dataframe(dati_Filtered2, use_container_width=True)

st.markdown(css_prova, unsafe_allow_html=True)