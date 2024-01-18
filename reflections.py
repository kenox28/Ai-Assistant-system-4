from nltk.chat.util import reflections

# Custom reflections
custom_reflections = {
    "myself": "yourself",
    "yourself": "myself",
    "my": "your",
    "your": "my",
    "I am": "you are",
    "you are": "I am",
    "I": "you",
    "you": "me",
}

# Merge with default reflections
reflections = {**reflections, **custom_reflections}