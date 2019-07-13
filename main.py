import en_core_web_sm

if __name__ == '__main__':
    nlp = en_core_web_sm.load()
    doc = nlp(u"Apple is looking at buying U.K. startup vacuum downtown for $1 billion")
    for chunk in doc.cats:
        print(chunk)

