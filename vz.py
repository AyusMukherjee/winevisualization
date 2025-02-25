pip install streamlit 
pip install pandas 
pip install seaborn 
pip install matplotlib
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Streamlit App Title
st.title("Wine Quality Data Explorer")

# Upload Dataset
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Dataset Preview")
    st.write(df.head())

    # Select columns for visualization
    st.write("### Select Variables for Visualization")
    x_axis = st.selectbox("Select X-axis variable", df.columns)
    y_axis = st.selectbox("Select Y-axis variable", df.columns)

    # Plot Scatter Plot
    st.write("### Scatter Plot")
    fig, ax = plt.subplots()
    sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    st.pyplot(fig)
    
    # Plot Histogram
    st.write("### Histogram")
    feature = st.selectbox("Select Feature for Histogram", df.columns)
    fig, ax = plt.subplots()
    sns.histplot(df[feature], bins=20, kde=True, ax=ax)
    st.pyplot(fig)
    
    # Correlation Heatmap
    st.write("### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig)
    
    st.success("Visualization complete!")
else:
    st.warning("Please upload a dataset to proceed.")
