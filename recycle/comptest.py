import codecs
import re

dicts = []
with codecs.open('../plain/pku_test_words.utf8', 'w', encoding='utf8') as wf:
    with codecs.open('../plain/pku_test.utf8', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            words = re.split(" ", line)
            for word in words:
                if len(word) > 0:
                    dicts.append(word)
        dicts.sort()
        for word in dicts:
            wf.write(word, "\n")
    print("FIN")
