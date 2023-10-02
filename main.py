import langchain_helper as lch
import streamlit as st

st.title("Pets name generator")

animal_type= st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow"))
if animal_type=="Cat":
    pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)
if animal_type=="Dog":
    pet_color = st.sidebar.text_area(label="What color is your Dog?", max_chars=15)
if animal_type=="Cow":
    pet_color = st.sidebar.text_area(label="What color is your Cow?", max_chars=15)

if pet_color:
    response = lch.generate_pet_name(animal_type, pet_color)
    st.text(response["pet_name"])
