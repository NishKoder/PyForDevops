import wikipedia
from textblob import TextBlob


def wiki(name="Python", length=1):
    return wikipedia.summary(name, sentences=length)


def search_wiki(name="Python"):
    return wikipedia.search(name)


def phrase(name):
    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
