import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

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


def display_recipe(recipe):
    st.title(recipe["title"])
    st.image(recipe["image"], use_column_width=True)
    st.subheader("Ingredients:")
    for ingredient in recipe["usedIngredients"]:
        st.write(f"- {ingredient['original']}")
    st.subheader("Missing Ingredients:")
    for ingredient in recipe["missedIngredients"]:
        st.write(f"- {ingredient['original']}")
    st.subheader("Instructions:")
    st.write(recipe["instructions"])

def main():
    st.set_page_config(page_title="Recipe Finder")

    ingredients = st.text_input("Enter the ingredients (comma-separated)")
    ingredients = [ingredient.strip() for ingredient in ingredients.split(",")]

    if ingredients:
        display_button = st.button("Get Recipes")

        if display_button:
            recipe_data = get_recipes_by_ingredients(ingredients.split(","))
            if recipe_data:
                for recipe in recipe_data:
                    st.write(f"Title: {recipe['title']}")
                    st.write(f"Image: {recipe['image']}")
                    st.write(f"Missing Ingredients: {recipe['missedIngredients']}")
                    st.write("---")
                else:
                    st.write("No recipes found.")
            else:
                st.warning("Please enter some ingredients.")

if __name__ == "__main__":
    main()
