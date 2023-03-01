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


sauls_keto_menu = []
with open("sauls_menu.json", "r") as fp:
    sauls_menu = json.load(fp)

# ipdb> sauls_menu[0]
# {'name': 'Hummus or Eggplant Appetizer', 'description': 'With tahini, parsley and pita'}
for idx in range(len(sauls_menu)):
    sleep(1)
    print(idx)

    dish_name = sauls_menu[idx]["name"]
    dish_description = sauls_menu[idx]["description"]

    PROMPT = f"""
            Decide whether a dish is keto friendly, and then give your rationale.

            Dish: salmon and argula
            Description:
            Keto: yes
            Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

            Dish: Saul's Burger
            Description: Grass-fed hamburger
            Keto: yes
            Rationale: a grass-fed hamburger can be part of a keto diet. Grass-fed beef is a great source of healthy fats and protein, and when served without a bun, it

            Dish: {dish_name}
            Description: {dish_description}
            Keto:
            Rationale:
            """

    response = openai.Completion.create(
        model="text-davinci-003", prompt=PROMPT, temperature=0, max_tokens=50
    )
    # pprint(response.to_dict_recursive)
    answer = response.choices[0]["text"].strip()
    sauls_keto_menu.append(
        {
            "1. dish name": dish_name,
            "2. dish description": dish_description,
            "3. AI's answer on keto": answer,
        }
    )

with open("sauls_keto_menu.json", "w") as fp:
    json.dump(sauls_keto_menu, fp, sort_keys=True, indent=4)