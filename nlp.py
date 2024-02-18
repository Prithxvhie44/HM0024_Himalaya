import pandas as pd
import nltk

# Downloaind models
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Parse the sentence using NLP to get keywords and amount
def getEntry(text):
    # Tokenize using nltk
    tokenized = nltk.word_tokenize(text
    # Perform POS Tagging using Penn Treebank codeset
    pos = nltk.pos_tag(tokenized)
    entry = identifyEntry(pos)
    return entry

def identifyEntry(tags):
    nouns = list()
    amount = None
    # Only keep nouns and cardinal number.
    # Noun is recognized by NNS, NN, NP, NPS
    # So we see if first letter is N, if yes, we add it to the tags.
    for item in tags:
        value, tag = item
        value = str(value)
        if tag.startswith('N'):
            nouns.append(value)
        if tag == 'CD':
            amount = value
    return nouns, amount

