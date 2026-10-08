import pandas as pd
import seaborn as sns
import streamlit as st

# Page Configuration
st.set_page_config(page_title="Fish Species Explorer", layout="wide")
st.title("🐟 Fish Species Data Explorer")

# 1. Load Data
@st.cache_data
def load_data():
    return pd.read_csv("fish_data.csv")

try:
    df = load_data()
except FileNotFoundError:
    st.error("Please ensure 'fish_data.csv' is in the same directory.")
    st.stop()

# 2. Sidebar Filters
st.sidebar.header("Filter Options")
species_list = ["All"] + list(df["species"].unique())
selected_species = st.sidebar.selectbox("Select Species", species_list)

# Filter dataframe based on selection
if selected_species != "All":
    filtered_df = df[df["species"] == selected_species]
else:
    filtered_df = df.copy()

# 3. Main Dashboard Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Data Overview")
    st.write(f"Total Records: {len(filtered_df)}")
    st.dataframe(filtered_df.head(10), use_container_width=True)
    
    st.subheader("Summary Statistics")
    st.write(filtered_df.describe().T[["mean", "min", "max"]])

with col2:
    st.subheader("Length vs Weight Analysis")
    fig = sns.pairplot(
        filtered_df, 
        vars=["length", "weight", "w_l_ratio"], 
        hue="species" if selected_species == "All" else None,
        diag_kind="kde"
    )
    st.pyplot(fig)