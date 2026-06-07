import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("AI Dashboard")

# Load Dataset
df = pd.read_csv("iris.csv")

# Dataset Overview
st.header("Dataset Overview")

st.write("First 5 Records")
st.dataframe(df.head())

st.write("Rows and Columns")
st.write(df.shape)

# Data Cleaning
st.header("Data Cleaning")

st.write("Missing Values")
st.write(df.isnull().sum())

st.write("Duplicate Rows")
st.write(df.duplicated().sum())

# KPIs
st.header("KPIs")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Rows",
    df.shape[0]
)

col2.metric(
    "Columns",
    df.shape[1]
)

col3.metric(
    "Missing Values",
    df.isnull().sum().sum()
)

# Filter
st.header("Filter")

species = st.selectbox(
    "Select Species",
    df["species"].unique()
)

filtered_df = df[
    df["species"] == species
]

st.dataframe(filtered_df)

# Chart 1
st.header("Species Count")

fig = px.histogram(
    df,
    x="species"
)

st.plotly_chart(fig)

# Chart 2
st.header("Sepal Length Distribution")

fig = px.histogram(
    df,
    x="sepal_length"
)

st.plotly_chart(fig)

# Chart 3
st.header("Petal Length Distribution")

fig = px.histogram(
    df,
    x="petal_length"
)

st.plotly_chart(fig)

# Chart 4
st.header("Sepal Length vs Petal Length")

fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species"
)

st.plotly_chart(fig)

# Chart 5
st.header("Petal Length by Species")

fig = px.box(
    df,
    x="species",
    y="petal_length"
)

st.plotly_chart(fig)