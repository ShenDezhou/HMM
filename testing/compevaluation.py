import codecs

GOLD = '../plain/pku_test_words.utf8'
HMM = '../plain/pku_test_hmm_words.utf8'

with codecs.open(GOLD, 'r', encoding='utf8') as wfa:
    gold = wfa.readlines()
    print(len(gold))
    with codecs.open(HMM, 'r', encoding='utf8') as wfb:
        hmm = wfb.readlines()
        print(len(hmm))
        N = len(gold)
        Cset = set(gold) - (set(gold) - set(hmm))
        print(Cset)
        C = len(Cset)
        Eset = set(hmm) - Cset
        print(Eset)
        E = len(Eset)
        R = float(C) / N
        P = float(C) / (C + E)
        print("Recall:", R)
        print("Precision", P)
        print("F1:", 2 * P * R / (P + R))
        print("ER:", float(E) / N)
