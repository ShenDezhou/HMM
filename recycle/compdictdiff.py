import codecs


def readdict(file):
    dicts = {}
    chars = []
    with codecs.open(file, 'r', encoding='utf8') as f:
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

    dicts = dict(zip(chars, range(1, len(chars) + 1)))
    return dicts


a, b = readdict("pku_dict.utf8"), readdict("../pku_dic/pku_dict.utf8")
d = list(set(b.keys()) - set(a.keys()))
print(d)
