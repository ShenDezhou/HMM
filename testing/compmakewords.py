import codecs

MODE = 2
if MODE == 1:
    INPUT = '../plain/pku_test_gold.utf8'
    OUTPUT = '../plain/pku_test_words.utf8'

if MODE == 2:
    INPUT = '../plain/pku_test_hmm.utf8'
    OUTPUT = '../plain/pku_test_hmm_words.utf8'

statenames = "BMES"
dicts = []
with codecs.open(OUTPUT, 'w', encoding='utf8') as wf:
    with codecs.open(INPUT, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip().split(" ")
            for word in words:
                if len(word) > 0:
                    dicts.append(word)
    dicts = list(set(dicts))
    dicts.sort()
    for word in dicts:
        wf.write(word)
        wf.write("\n")

    print("FIN")
