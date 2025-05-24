import streamlit as st
import pandas as pd

st.title("Job Listing Clusters")

df = pd.read_csv('clustered_jobs.csv')
st.write("Columns in dataset:", list(df.columns))  # Debugging: See what columns exist

if 'Cluster' in df.columns:
    clusters = df['Cluster'].unique()
    cluster_selected = st.sidebar.multiselect("Select clusters", clusters)

    if cluster_selected:
        filtered = df[df['Cluster'].isin(cluster_selected)]
        st.write(filtered)
    else:
        st.write(df)
else:
    st.error("The 'Cluster' column is not found in the uploaded dataset.")
    st.write(df)
