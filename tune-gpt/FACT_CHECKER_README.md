# Example USAGE

```
python fact-checker/fact_checker.py "Is a grass-fed hamburger part of the keto diet?"
```

# Examples

```
"Does a grass-fed hamburger contain healthy omega-3 fats?"
"What is the glycemic index grass-fed hamburger?"
"Can high-glycemic carbohydrates be removed from a grass-fed hamburger?"
"How can a grass-fed hamburger be made for a person on a keto diet?"
"How can pure corn syrup be made for a person on a keto diet?"
"Can pure corn syrup be prepared for a person on a keto diet?"
"Can a grass-fed hamburger be prepared for a person on a keto diet?"
```

# fact checking with prompt chaining

This repo is a simple demonstration of using [langchain](https://github.com/hwchase17/langchain) to do fact-checking with prompt chaining. How it works:
- you ask your desired LLM a question
- the LLM generates an initial answer to the question
- the LLM self-interrogates what the assumptions were that went into that answer
- the LLM sequentially determines if each of these assumptions are true
- the LLM generates a new answer to the question, incorporating the new information

## to run

Make sure you have langchain installed (`pip install langchain`). Then run

`python3 fact_checker.py 'insert question here'`

*Be sure to wrap your question in quotes if you're passing it as a command line argument.*

Alternatively, you can use the provided `fact_checker.ipynb` notebook.

## example

Question: *"What type of mammal lays the biggest eggs?"*


**Initial answer:**
The biggest eggs laid by any mammal belong to the elephant.

**Assumptions made:**
- The elephant is a mammal 
- Mammals lay eggs 
- Eggs come in different sizes 
- Elephants lay bigger eggs than other mammals

**Verification of assumptions:**
- The elephant is a mammal: TRUE 
- Mammals lay eggs: FALSE - Most mammals give birth to live young.
- Eggs come in different sizes: TRUE 
- Elephants lay bigger eggs than other mammals: FALSE - Elephants do not lay eggs.

**New answer:**
This question cannot be answered because elephants do not lay eggs and most mammals give birth to live young.

## credits
Proof of concept by [Jasper](https://twitter.com/0xjasper)

Huge thanks to @hwchase17 and the langchain project!
