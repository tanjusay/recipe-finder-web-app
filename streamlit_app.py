import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

st.title("Recipe Finder")
st.header("Find Delicious Recipes!")

ingredients = st.text_input("Enter the ingredients you have (comma-separated):")

if st.button("Search Recipes"):
    response = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={ingredients}&apiKey={api_key}")

    if response.status_code == 200:
        data = response.json()
        print(data)
        recipes = data["results"]

        for recipe in recipes:
            st.subheader(recipe["title"])
            st.image(recipe["image"], caption="Recipe Image")
            st.write("Ingredients:", ", ".join(recipe["missedIngredients"]))
            #st.write("Instructions:", recipe["instructions"])
            st.markdown("---")
    else:
        st.error("Error retrieving recipes. Please try again later.")
