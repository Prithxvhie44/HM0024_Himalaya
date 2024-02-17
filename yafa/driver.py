from yafa import speechlib
import pandas as pd
import nltk

def start():
    text = speechlib.getPhrase()
    if text == None:
        print("ERROR: Some error occured while speech to text.")
        exit(1)
    tokenized = nltk.word_tokenize(text)
    pos = nltk.pos_tag(tokenized)
    entry = identifyEntry(pos)

def identifyEntry(tags):
    nouns = list()
    amount = None
    for item in tags:
        value, tag = item
        value = str(value)
        if tag.startswith('N'):
            nouns.append(value)
        if tag == 'CD':
            amount = int(value)
    return nouns, amount

