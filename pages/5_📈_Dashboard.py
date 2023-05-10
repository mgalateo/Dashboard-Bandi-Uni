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
        width: 300px;
}

#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div:nth-child(5) > div > div{
    place-content: center;
}

[data-testid="stAppViewContainer"]{
    background-image: url(https://images5.alphacoders.com/129/1297020.png);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}
[id="dashboard"]{
    font-size: 72px;
    color: crimson;
    text-shadow: -1px 0 snow, 0 1px snow, 1px 0 snow, 0 -1px snow;
}
[id="il-progetto-pi-longevo"]{
    color: mintcream;
}

[id="bando-con-pi-risorse"]{
    color: mintcream;
}


[id="nazione-che-ha-stanziato-pi-fondi"]{
    color: mintcream;
}

[id="area-con-pi-fondi-stanziati"]{
    color: mintcream;
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
[data-testid="metric-container"]{
    background-color: snow;
    padding: 20px;
    border-radius: 20px;
   
}
[data-testid="collapsedControl"]{
    background-color: chartreuse;
    padding: 20px;
    border-radius: 20px;
   
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(1) > div:nth-child(1) > div > div > div > label > div > div > p{
    font-size: x-large;
    color: crimson;
}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section.main.css-uf99v8.egzxvld5 > div.block-container.css-z5fcl4.egzxvld4 > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v3 > div:nth-child(2) > div:nth-child(1) > div > div > div > label > div > div > p{
   font-size: x-large;
    color: crimson;
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



st.title("Dashboard 📈")

###Lettura Dataset
local_filename = 'Dataset_Bandi.xlsx'

dati = pd.read_excel(local_filename)






### Filter sidebar
st.sidebar.header("Filtri")




funder_country = st.sidebar.text_input('Seleziona Paese', '')

paesi = st.sidebar.multiselect(
    "Aree",
    options=dati["Funder Country"].unique(),
    default=dati["Funder Country"].unique()
)

aree = st.sidebar.multiselect(
    "Aree",
    options=dati["Units of Assessment"].unique(),
    default=dati["Units of Assessment"].unique()
)


if (len(funder_country) != 0):
    df_filtered = dati[
        (dati["Funder Country"].isin(paesi)) &
        (dati["Units of Assessment"].isin(aree)) &
        (dati['Funder Country'] == funder_country)
        ]


else :
    df_filtered = dati[
        (dati["Funder Country"].isin(paesi)) &
        (dati["Units of Assessment"].isin(aree))
        ]

totale_fundingd = dati['Funding Amount in EUR'].sum()
totale_funding = df_filtered['Funding Amount in EUR'].sum()
num_elementid = dati.shape[0]
num_elementi = df_filtered.shape[0]


col1, col2 = st.columns(2)

with col1:
   st.metric(label="Totale Fondi", value=totale_funding, delta=totale_funding-totale_fundingd)
with col2:
   st.metric(label="Bandi", value=num_elementi, delta=num_elementi-num_elementid)










# converte le colonne Start Date e End Date in oggetti datetime
df_filtered["Start Date"] = pd.to_datetime(df_filtered["Start Date"].fillna('2000-1-1'))
df_filtered["End Date"] = pd.to_datetime(df_filtered["End Date"].fillna('2000-1-1'))

# calcola la durata in giorni e aggiungi la colonna al dataset
df_filtered["durata"] = (df_filtered["End Date"] - df_filtered["Start Date"]).dt.days

# mostra la riga con la durata maggiore
riga_max_durata = df_filtered.loc[df_filtered["durata"].idxmax()]

# Creiamo un nuovo dataframe con la riga selezionata
df_max_dur = pd.DataFrame(riga_max_durata).transpose()

st.title('✅Il progetto più longevo')
st.dataframe(df_max_dur, use_container_width=True)

st.title('✅Nazione che ha stanziato più fondi')

df_sum_country = df_filtered.groupby("Funder Country").agg({"Funding Amount in EUR": "sum"})
df_sum_country = df_sum_country.reset_index()
df_sum_county_sorted = df_sum_country.sort_values("Funding Amount in EUR", ascending=False)

base1="./Assets/"
nation0 = df_sum_county_sorted.iloc[0]["Funder Country"]
nation1=nation0.lower()
path1= base1 + nation1 + ".png"




image1 = Image.open(path1)
st.image(image1)


st.dataframe(df_sum_county_sorted, use_container_width=True)



st.title('✅Bando con più risorse')
# mostra la riga con più fondi
riga_max_funding = df_filtered.loc[df_filtered["Funding Amount in EUR"].idxmax()]
# Creiamo un nuovo dataframe con la riga selezionata
df_max_dur = pd.DataFrame(riga_max_funding).transpose()

base="./Assets/"
nation=df_max_dur["Funder Country"].values[0].lower()
path= base + nation + ".png"




image = Image.open(path)
st.image(image)


st.dataframe(df_max_dur)

st.title('✅Area con più fondi stanziati')

df_sum = df_filtered.groupby("Units of Assessment").agg({"Funding Amount in EUR": "sum"})
df_sum_sorted = df_sum.sort_values("Funding Amount in EUR", ascending=False)
first_row = df_sum_sorted.head(1)


st.dataframe(first_row, use_container_width=True)

st.markdown(css_prova, unsafe_allow_html=True)