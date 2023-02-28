"""
Source: OpenAI docs

Fine-tune a classification model on a custom dataset

https://github.com/openai/openai-cookbook/blob/main/examples/Fine-tuned_classification.ipynb
"""

from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import openai

categories = ["rec.sport.baseball", "rec.sport.hockey"]
sports_dataset = fetch_20newsgroups(
    subset="train", shuffle=True, random_state=42, categories=categories
)

print(sports_dataset["data"][0])
