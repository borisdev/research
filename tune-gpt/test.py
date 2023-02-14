import os
import openai
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Say this is a test",
    temperature=0,
    max_tokens=7
)

pprint(response.to_dict_recursive)

"""
response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Is salmon and arugula a keto dish?",
    temperature=0,
    max_tokens=40
)
pprint(response.to_dict_recursive)

PROMPT = '''
        Decide whether a dish is keto, and then give your rationale.

        Dish: salmon and argula
        Keto: yes
        Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

        Dish: bagel and argula
        Keto:
        Rationale:
        '''

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=PROMPT,
    temperature=0,
    max_tokens=40
)
pprint(response.to_dict_recursive)
"""


PROMPT = '''
        Decide whether a dish is keto, and then give your rationale.

        Dish: salmon and argula
        Keto: yes
        Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

        Dish: Grass-fed hamburger
        Keto:
        Rationale:
        '''

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=PROMPT,
    temperature=0,
    max_tokens=40
)
pprint(response.to_dict_recursive)
