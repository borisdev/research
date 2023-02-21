# Fine-tune GPT


```
pip install -r requirements.txt
python open_ai_test.py
```


# TODOs

- [ ] [Menu's in Google Business Profile API](https://developers.google.com/my-business/reference/rest/v4/FoodMenus)

# Examples

1. Prompt

```
Is salmon and arugula a keto dish?
```

1. Response

```
Yes, salmon and arugula can be part of a keto diet.
Salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.
```

2. Prompt

```
Decide whether a dish is keto, and then give your rationale.

Dish: salmon and argula
Keto: yes
Rationale: Because salmon is a great source of healthy fats and protein, while arugula is a low-carb vegetable.

Dish: bagel and argula
Keto:
Rationale:

```

Response

```
No, because a bagel is high in carbohydrates and not suitable for a keto diet.
```

# References

- [prompt design](https://platform.openai.com/docs/guides/completion/prompt-design)
- [OpenAI Libraries](https://platform.openai.com/docs/libraries)
