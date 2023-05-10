###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image




###Informazioni Pagina
st.set_page_config(
    page_title="Bandi",
    page_icon="📑",
    layout="wide"
)



st.title("Bandi")


image = Image.open('./Assets/ricerca.jpg')
st.image(image)



###Lettura Dataset
local_filename = 'Dataset_Bandi.xlsx'

dati = pd.read_excel(local_filename)

st.dataframe(dati)





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
[id="bandi"]{
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






</style>

"""

st.markdown(css_prova, unsafe_allow_html=True)