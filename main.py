from code_domain_emissary.emissary import Emissary

if __name__ == '__main__':
    em = Emissary()
    doc = em.process("create a function named get user account with the arguments user ID and include savings")
    print(doc.ents)
    print(list(doc.noun_chunks))
    for t in doc:
        print(t, [child for child in t.children], t.dep_, t.pos_)

