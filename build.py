from mindmeld import configure_logs
from mindmeld.components.nlp import NaturalLanguageProcessor

if __name__ == '__main__':
    configure_logs()
    nlp = NaturalLanguageProcessor("./code_domain_emissary")
    nlp.build()

    res1 = nlp.process("hello")
    assert res1.get("intent") == "greet"

    res2 = nlp.process("bye")
    try:
        assert res2.get("intent") == "exit"
    except AssertionError:
        print("Did not match intent: {}".format(res2.get("intent")))

    res3 = nlp.process("how")
    try:
        assert res3.get("intent") == "confused"
    except AssertionError:
        print("Did not match intent: {}".format(res2.get("intent")))
