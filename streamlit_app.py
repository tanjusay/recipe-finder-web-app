import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

API_KEY = os.getenv("SPOONACULAR_API_KEY")

def get_recipes_by_ingredients(ingredients):
    url = "https://api.spoonacular.com/recipes/findByIngredients"
    params = {
        "apiKey": API_KEY,
        "ingredients": ",".join(ingredients),
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    return None

st.title("Find Recipes by Ingredients")

ingredients = st.text_input("Enter ingredients separated by commas")

if ingredients:
    display_button = st.button("Get Recipes")

    if display_button:
        recipe_data = get_recipes_by_ingredients(ingredients.split(","))
        if recipe_data:
            for recipe in recipe_data:
                st.write(f"Title: {recipe['title']}")
                st.image(recipe['image'])
                st.write(f"Missing Ingredients: {', '.join([ingredient['name'] for ingredient in recipe['missedIngredients']])}")
                st.write("---")
        else:
            st.write("No recipes found.")
