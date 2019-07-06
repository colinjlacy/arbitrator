from mindmeld import configure_logs
from mindmeld.components.nlp import NaturalLanguageProcessor

if __name__ == '__main__':
    configure_logs()
    nlp = NaturalLanguageProcessor("./code_domain_emissary")
    nlp.build()

    res4 = nlp.process("bye")
    # res5 = nlp.process("Good bye!")
    # res6 = nlp.process("quit")

    assert res4.get("intent") == "delete_element"
    # assert res5.get("intent") == "delete_element"
    # assert res6.get("intent") == "delete_element"

    # res1 = nlp.process("hello")
    # res2 = nlp.process("hello?")
    # res3 = nlp.process("Hello!")
    #
    # assert res1.get("intent") == "edit_element"
    # assert res2.get("intent") == "edit_element"
    # assert res3.get("intent") == "edit_element"

