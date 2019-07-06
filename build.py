from mindmeld import configure_logs
from mindmeld.components.nlp import NaturalLanguageProcessor

configure_logs()
nlp = NaturalLanguageProcessor("./code_domain_emissary")
nlp.build()

if __name__ == '__main__':
    res1 = nlp.process("hello")
    res2 = nlp.process("hello?")
    res3 = nlp.process("Hello!")
    assert res1.get("intent") == "create_element"
    assert res2.get("intent") == "create_element"
    assert res3.get("intent") == "create_element"
