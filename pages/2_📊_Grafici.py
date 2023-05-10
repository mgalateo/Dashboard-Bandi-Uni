###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
import datetime as dt
from dateutil.relativedelta import relativedelta
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
[id="grafici"]{
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



st.title("Grafici 📊")



###Lettura Dataset
local_filename = 'Dataset_Bandi.xlsx'

dati = pd.read_excel(local_filename)


###fig = px.pie(dati, values='Quantita', names='Genere', title='Film per genere')
###st.plotly_chart(fig, use_container_width=True)

# Ordina i valori di Funder in ordine decrescente di occorrenze
funder_counts = dati["Funder"].value_counts()
funder_order = funder_counts.index.tolist()

# Crea l'istogramma
fig = px.histogram(dati, x="Funder",color="Funder" , text_auto=True, title="Occorrenze per Ente",
                   category_orders={"Funder": funder_order})

# Mostra l'istogramma su Streamlit
st.plotly_chart(fig, use_container_width=True)

# Ordina i valori di Funder Country in ordine decrescente di occorrenze
funderC_counts = dati["Funder Country"].value_counts()
funderC_order = funderC_counts.index.tolist()

# Crea l'istogramma
fig2 = px.histogram(dati, x="Funder Country",color="Funder Country" , text_auto=True, title="Occorrenze per Paese",
                   category_orders={"Funder Country": funderC_order})

# Mostra l'istogramma su Streamlit
st.plotly_chart(fig2, use_container_width=True)

# Ordina i valori di Units of Assessment in ordine decrescente di occorrenze
ua = dati["Units of Assessment"].value_counts()
ua_order = ua.index.tolist()

# Crea l'istogramma
fig3 = px.histogram(dati, y="Units of Assessment",color="Units of Assessment" , text_auto=True, title="Occorrenze per Area",
                   category_orders={"Units of Assessment": ua_order})

# Mostra l'istogramma su Streamlit
st.plotly_chart(fig3, use_container_width=True)

st.markdown(css_prova, unsafe_allow_html=True)