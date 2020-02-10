import codecs

dicts = {}
chars = []
with codecs.open('pku_training.utf8', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        for ch in line:
            if ch == ' ':
                continue
            else:
                chars.append(ch)
# make char dictionaryy
chars = list(set(chars))
print(len(chars))
with codecs.open('pku_dict.utf8', 'w', encoding='utf8') as f:
    for c in chars:
        f.write(c)

dicts = dict(zip(chars, range(1, len(chars) + 1)))

with codecs.open('pku_seq.txt', 'w', encoding='utf8') as wf:
    with codecs.open('pku_training.utf8', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            seq = ""
            for ch in line:
                if ch == ' ':
                    continue
                else:
                    seq += str(dicts[ch]) + ','
            wf.write(seq + "\n")
    print("FIN")
