# Fine-tune GPT


```
pip install -r requirements.txt
python open_ai_test.py
```
# Mics ideas

- Food match
- Diet match
- Dish score
- Keto score
- Your diet, your food
- my food
- Search for food that matches your special dietary requirements
- Search for restaurants that matches your special dietary requirements

# TODOs

- [ ] Lookup file of all grass-fed beef producers
- [ ] Apply to affiliate programs (Re-apply to GrubHub)

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
