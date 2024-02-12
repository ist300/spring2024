import streamlit as st

# Creating Containers 
header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()
model_Training = st.beta_container()


# Adding Content to Containers
with header:
    st.title("Testing")
    st.text("I am ...")
    
with dataset:
    st.header("NYC taxi dataset")
    
    