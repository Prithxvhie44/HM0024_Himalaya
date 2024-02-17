import pandas as pd
import nltk

def getEntry(text):
    tokenized = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokenized)
    entry = identifyEntry(pos)
    return entry

def identifyEntry(tags):
    nouns = list()
    amount = None
    for item in tags:
        value, tag = item
        value = str(value)
        if tag.startswith('N'):
            nouns.append(value)
        if tag == 'CD':
            amount = value
    return nouns, amount

