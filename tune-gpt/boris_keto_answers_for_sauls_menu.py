"""
Transforms the data from sauls_keto_menu.json into a CSV file for Boris to
classify menu items as keto friendly or not.

Source data: sauls_keto_menu.json

[
    {
        '1. dish name': 'Blintz',
        '2. dish description': '',
        "3. AI's answer on keto": 'No, blintz is not keto friendly. Blintzes are '
                            'usually made with a crepe-like batter that is '
                            'high in carbohydrates, making them not suitable '
                            'for a keto diet.'}
    },{...
]

Final sheet: https://docs.google.com/spreadsheets/d/17y8m5SHEQEgGIT9oIT7wgaZf3awpnnzao-ajDgxuiM4/edit?usp=sharing
"""
import json
import csv


class Dish:
    """Class for keeping track of an item in inventory."""

    def __init__(self, item):
        self.name = item["1. dish name"]
        self.desc = item["2. dish description"]
        self.ai = item["3. AI's answer on keto"]


with open("sauls_keto_menu.json") as f:
    sauls_keto_menu = json.load(f)


with open("boris_keto_answers_for_sauls_menu.csv", "w") as csvfile:
    fieldnames = ["name", "desc", "ai"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="|")
    writer.writeheader()
    for item in sauls_keto_menu:
        dish = Dish(item)
        print(dish.name, dish.desc, dish.ai)
        writer.writerow({"name": dish.name, "desc": dish.desc, "ai": dish.ai})
