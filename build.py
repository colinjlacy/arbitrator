from mindmeld import configure_logs
from mindmeld.components.nlp import NaturalLanguageProcessor

if __name__ == '__main__':
    configure_logs()
    nlp = NaturalLanguageProcessor("./code_domain_emissary")
    nlp.build()

    res1 = nlp.process("hello")
    assert res1.get("intent") == "create_element"

    res2 = nlp.process("bye")
    assert res2.get("intent") == "delete_element"
