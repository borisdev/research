"""
Make this a Jupyter notebook
"""

import os
import openai
from dotenv import load_dotenv
from pprint import pprint

# import ipdb
import json
from time import sleep

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")

prompts = [
    "Is salmon and arugula a keto dish?",
    """
        Decide whether a dish is keto, and then give your rationale.

        Dish: salmon and argula
        Keto: yes
        Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

        Dish: bagel and argula
        Keto:
        Rationale:
    """,
    """
        Decide whether a dish is keto, and then give your rationale.

        Dish: salmon and argula
        Keto: yes
        Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

        Dish: Grass-fed hamburger
        Keto:
        Rationale:
    """,
    """
        Decide whether a dish is keto friendly, and then give your rationale.

        Dish: salmon and argula
        Description:
        Keto: yes
        Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

        Dish: Saul's Burger
        Description: Grass-fed hamburger
        Keto: yes
        Rationale: a grass-fed hamburger can be part of a keto diet. Grass-fed beef is a great source of healthy fats and protein, and when served without a bun, it

        Dish: Hummus or Eggplant Appetizer
        Description: With tahini, parsley and pita
        Keto:
        Rationale:
    """,
    """
        Given a dish and its ingredients, list the ingredients that are substitutable and not
        substitutable in the dish.

        Dish: hamburger and fries
        Ingredients: beef patty, bun, fries
        Substitutable: bun, fries
        Not substitutable: beef patty

        Dish: fish and chips
        Ingredients: Fish fillet, potatoes, oil for frying
        Substitutable: potatoes
        Not substitutable: Fish fillet, oil for frying

        Dish: {dish}
        Ingredients: {ingredients}
        Substitutable:
        Not substitutable:
    """,
]

# FAILED EXPERIMENT --> What ingredients in the dish are removable?

prompt = """
        What ingredients in the dish can be subsituted out?

        Dish: hamburger and fries
        Ingredients: beef patty, bun, fries
        Removable: bun, fries

        Dish: fish and chips
        Ingredients: Fish fillet, potatoes, oil for frying
        Removable: potatoes

        Dish: Plain Pizza
        Ingredients: bread, cheese, tomato sauce
        Removable: none

        Dish: {dish}
        Ingredients: {ingredients}
        Removable:
        """


class Meal:
    def __init__(self, dish, ingredients):
        self.dish = dish
        self.ingredients = ingredients

    def __repr__(self):
        return f"meal(dish={self.dish}, ingredients={self.ingredients})"


# split on AND

meals = [
    Meal("Cheese Pizza", "bread, cheese, tomato sauce"),
    Meal("Chicken Parmesan", "chicken, bread, tomato sauce, cheese"),
    Meal("Chicken and Waffles", "chicken, waffles, syrup"),
    Meal("Hot dog", "hot dog, bun"),
    Meal("Fries", "potatoes, oil for frying"),
    Meal("Pizza", "bread, cheese, tomato sauce"),
]

for meal in meals:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt.format(dish=meal.dish, ingredients=meal.ingredients),
        temperature=0,
        max_tokens=60,
    )
    answer = response.choices[0]["text"].strip()

    print("=========")
    print("dish:", meal.dish)
    print("ingredients:", meal.ingredients)
    print("answer:", answer)
