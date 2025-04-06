import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Simple Data Dashboard")

upload_file = st.file_uploader("Choose a CSV file", type="csv")


if upload_file is not None:
    df = pd.read_csv(upload_file)
    

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader('Filter Data')
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value to filter", unique_values)

    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    st.subheader("Plot Data")
    X_column = st.selectbox("Select X-axis column", columns)
    Y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        st.line_chart(filtered_df.set_index(X_column)[Y_column])

else:
    st.write("Waiting fo file upload...")