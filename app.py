import streamlit as st

# Title
st.title("My First Streamlit App")

# Header
st.header("Welcome Shanthi 👋")

# Text
st.write("This is a simple Streamlit UI example.")

# Input box
name = st.text_input("Enter your name:")

# Button
if st.button("Submit"):
    st.success(f"Hello {name}! Welcome to Streamlit 🚀")

# Slider
age = st.slider("Select your age:", 0, 100, 19)

st.write("Your age is:", age)

# Checkbox
if st.checkbox("Show message"):
    st.info("You are learning Streamlit UI!")
