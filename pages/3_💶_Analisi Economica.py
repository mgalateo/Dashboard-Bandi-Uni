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
[id="analisi-economica"]{
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



st.title("Analisi Economica 💶")



###Lettura Dataset
local_filename = 'Dataset_Bandi.xlsx'

dati = pd.read_excel(local_filename)

# Crea il grafico a torta
fig = px.pie(dati, values="Funding Amount in EUR",color="Funder", names="Funder Country", title="Somma dei finanziamenti per ogni Funder")

# Mostra il grafico a torta su Streamlit
st.plotly_chart(fig, use_container_width=True)

# Crea il grafico a torta
fig2 = px.pie(dati, values="Funding Amount in EUR",color="Funder", names="Funder", title="Somma dei finanziamenti per ogni Funder")

# Mostra il grafico a torta su Streamlit
st.plotly_chart(fig2, use_container_width=True)

# elimina le righe con valori null nella colonna "Units of Assessment"
datifiltered = dati.dropna(subset=['Units of Assessment'])

# Crea il grafico a torta
fig3 = px.pie(datifiltered, values="Funding Amount in EUR",color="Units of Assessment", names="Units of Assessment", title="Somma dei finanziamenti per ogni Area")

# Mostra il grafico a torta su Streamlit
st.plotly_chart(fig3, use_container_width=True)



st.markdown(css_prova, unsafe_allow_html=True)