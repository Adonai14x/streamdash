import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Car Sales Dashboard")

df = pd.read_csv("vehicles.csv")

st.write("Car Sales Data Overview", df.head())

px.histogram(df, x="make", title="Car Sales by Make").show()

px.scatter(df, x="year", y="price", color="make", title="Car Price by Year and Make").show()

st.plotly_chart(px.histogram(df, x="make", title="Car Sales by Make"))

if.st.checkbox("Show Data Table"):
    st.dataframe(df)
    filtered = df[df["make"] == st.selectbox("Select Make", df["make"].unique())]
    st.write(filtered.head())