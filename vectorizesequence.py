import codecs

dicts = {}
chars = []


def readchar(file):
    chars = []
    with codecs.open(file, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            for ch in line:
                if ch == ' ' or ch == '\r' or ch == '\n':
                    continue
                else:
                    chars.append(ch)
    return chars


chars.extend(readchar("plain/pku_training.utf8"))
# chars.extend(readchar("plain/pku_test.utf8"))


# make char dictionaryy
chars = list(set(chars))
chars.sort()
print(len(chars))
with codecs.open('pku_dic/pku_dict.utf8', 'w', encoding='utf8') as f:
    for c in chars:
        f.write(c)

dicts = dict(zip(chars, range(1, (len(chars) + 1))))

with codecs.open('matlab/pku_train_vec_seq.txt', 'w', encoding='utf8') as wf:
    with codecs.open('plain/pku_training.utf8', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            seq = ""
            for ch in line:
                if ch == ' ' or ch == '\r' or ch == '\n':
                    continue
                else:
                    seq += str(dicts[ch]) + ','
            wf.write(seq + "\n")
    print("FIN")
