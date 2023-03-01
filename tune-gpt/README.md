# Fine-tune GPT


[Boris labeled Saul's menu as keto](https://docs.google.com/spreadsheets/d/17y8m5SHEQEgGIT9oIT7wgaZf3awpnnzao-ajDgxuiM4/edit?usp=sharing)

# GPT's open source competitor BLOOM

- [BLOOM 176B — how to run a real LARGE language model in your own cloud?](https://medium.com/mlearning-ai/bloom-176b-how-to-run-a-real-large-language-model-in-your-own-cloud-e5f6bdfb3bb1)

# A chain three AI prompts and two computes to derive the keto score

1. AI prompt: "List all items in dish"
2. AI prompt: "List what removable items from dish" 
3. compute: modified dish items = list of new meal items = initial meal - removed high carb meal items
4. AI prompt: nutritional breakdown - get calories, fat, carbs, and fiber of each item
5. compute: keto score = % good fat grams - % (carbs grams - fiber grams) [of modified dish]



## Mission

- Your diet, your food
- Search for food that matches your special dietary requirements
- Search for restaurants that matches your special dietary requirements

# Ideas 

# Approach standard: Pre-compute all predictions

- keto
- halal
- vegetarian

# Approach deluxe: Let the user be free to write their own prompts

Fine-tune examples and indexing a corpus in order to let user use their own prompts, such as

- "Where can I eat keto food with no dairy, no nuts and no gluten?"
- "Where can I eat halal food in the bay area?"
- "When can I eat keto, vegetarian food in Oakland?" 

# Approach personalized

- Train a model for each customer using [Steamship](https://medium.com/steamship/steamship-heroku-for-language-ai-9c7dd70cd25a)


# Tools

- MLFlow [How to Efficiently Fine-Tune your Machine Learning Models](https://towardsdatascience.com/how-to-fine-tune-your-machine-learning-models-with-ease-8ca62d1217b1)

# Names

- Meal Score(s)
- Dish Score(s)
- Alpha Score(s)
- Geo Score(s)
- Keto Score

```
meal scores by keto
```

```
Sure! The ketogenic diet is a low-carb, high-fat diet that has been used for
centuries to treat various medical conditions. It has been found to be effective
in weight loss and improving overall health. The main goal of the ketogenic diet
is to put your body into a state of ketosis, where it is burning fat for energy
instead of carbohydrates.

Meal scores on the ketogenic diet can vary depending on the individual.
Generally, the higher the fat content of the meal, the higher the score. It is
important to note that the ketogenic diet is not a one-size-fits-all approach,
and that different people may respond differently to different foods. For
example, some people may find that they do better with higher-fat meals, while
others may find that they do better with lower-fat meals.

In addition to the fat content of the meal, the macronutrient ratio of the meal
is also important. The ketogenic diet typically requires a ratio of 4:1 fat to
protein and carbohydrates. This means that for every 4 grams of fat, there
should be 1 gram of protein and carbohydrates. This ratio helps to keep the body
in a state of ketosis, which is necessary for the diet to be effective.

Finally, it is important to note that the ketogenic diet is not a “quick fix”
and requires a commitment to healthy eating habits. It is important to ensure
that you are getting enough vitamins and minerals in your diet, as well as
enough calories to maintain a healthy weight. ```
```


# TODOs

- [ ] compound classification: good fat AND net carb (low glycemic)
- [ ] Jupyter notebook to show/share my development work

## Nuanced examples

- hamburger, yes if removed bread
- cup of bad oil, no
- chicken soup, yes, if no noodles
- lamb byriani, maybe
- Palella, not really

## Future TODOs

- [ ] Lookup file of all grass-fed beef producers
- [ ] Apply to affiliate programs (Re-apply to GrubHub)


## Best Practices

- end question prompt with a ### to ensure the model does not predict a continuation 
- 'Say "I don't know" if you do not know the answer'
- high quality, diverse examples
- "The following answer is correct, high-quality, and written by an expert."
- "Let's think step by step" and "Give an  explanation of your reasoning before
  the final answer"

Sources:

- [Guide: How to work with large language models](https://github.com/openai/openai-cookbook/blob/main/how_to_work_with_large_language_models.md)
- [Techniques to improve reliability](https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md)

## References

[openai-cookbook](https://github.com/openai/openai-cookbook)

- Vector databases
- GPT-3
  - Guide: How to work with large language models
  - Guide: Techniques to improve reliability
  - How to use a multi-step prompt to write unit tests

- Embeddings
  - Text comparison examples
  - How to get embeddings
  - Question answering using embeddings

- Fine-tuning GPT-3
  - Guide: best practices for fine-tuning GPT-3 to classify text
  - Fine-tuned classification

OpenAI docs

- [prompt design](https://platform.openai.com/docs/guides/completion/prompt-design)
- [OpenAI Libraries](https://platform.openai.com/docs/libraries)
