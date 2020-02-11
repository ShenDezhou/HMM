import codecs

with codecs.open('pku_states.txt', 'w', encoding='utf8') as wf:
    with codecs.open('pku_training.utf8', 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            words = line.split(' ')
            state = ""
            for word in words:
                if len(word) == 0 or word == "\r\n":
                    continue
                if len(word) - 2 < 0:
                    state += 'S'
                else:
                    state += "B" + "M" * (len(word) - 2) + "E"
            wf.write(state + "\n")
    print("FIN")
