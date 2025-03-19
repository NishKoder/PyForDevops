import wikipedia


def wiki(name="Python", length=1):
    return wikipedia.summary(name, sentences=length)
