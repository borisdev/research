# Fine-tune GPT


[Boris labeled Saul's menu as keto](https://docs.google.com/spreadsheets/d/17y8m5SHEQEgGIT9oIT7wgaZf3awpnnzao-ajDgxuiM4/edit?usp=sharing)


# A chain three AI prompts and two computes

- compute final formula = percentage of calories from healthy fats of plated items - percent from high glycemic carbs
- query AI nutritional breakdown - get calories of each item, fat of each item, carbs of each item
- compute list of plated non carb meal items = initial meal - removed high carb meal items
- query AI what is removable as a list
- query AI get all items on plate as a list



## Mission

- Your diet, your food
- my food
- Search for food that matches your special dietary requirements
- Search for restaurants that matches your special dietary requirements

# Ideas 

- Train a model for each customer using [Steamship](https://medium.com/steamship/steamship-heroku-for-language-ai-9c7dd70cd25a)

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

- compound classification: good fat AND net carb (low glycemic)
- Jupyter notebook to show/share my development work

## Nuanced examples

- hamburger, yes if removed bread
- cup of bad oil, no
- chicken soup, yes, if no noodles
- lamb byriani, maybe
- Palella, not really

## Future TODOs

- [ ] Lookup file of all grass-fed beef producers
- [ ] Apply to affiliate programs (Re-apply to GrubHub)

## References

- [prompt design](https://platform.openai.com/docs/guides/completion/prompt-design)
- [OpenAI Libraries](https://platform.openai.com/docs/libraries)
