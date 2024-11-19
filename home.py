import streamlit as st
import pandas as pd

st.title("♟♟Website Developing using Python♟♟")
st.header("🐷🐷Website Developing using Python🐷🐷")

st.image('./img/sikawat.jpg')
st.subheader("Sikawat Loksutthi")

dt=pd.read_csv('./data/iris-3.csv')
st.header()
st.write(dt.head(10))