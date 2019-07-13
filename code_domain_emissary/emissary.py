import en_core_web_sm

class Emissary:

    def __init__(self):
        pass

    def process(self, text=""):
        nlp = en_core_web_sm.load()
        doc = nlp(u"{}".format(text))
        return doc
