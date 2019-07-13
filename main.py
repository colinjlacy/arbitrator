from code_domain_emissary.emissary import Emissary

if __name__ == '__main__':
    em = Emissary()
    doc = em.process("My name is Colin")
    print(doc)

