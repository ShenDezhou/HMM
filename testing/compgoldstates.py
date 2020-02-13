import codecs

MODE = 4

if MODE == 1:
    INPUT = 'plain/pku_training.utf8'
    OUTPUT = 'state/gold/pku_train_states.txt'

if MODE == 2:
    INPUT = 'plain/pku_test_gold.utf8'
    OUTPUT = 'state/gold/pku_test_states.txt'

if MODE == 3:
    INPUT = 'plain/pku_training_words.utf8'
    OUTPUT = 'state/gold/pku_train_words_states.txt'

if MODE == 4:
    INPUT = 'plain/pku_test_words.utf8'
    OUTPUT = 'state/gold/pku_test_words_states.txt'

with codecs.open(OUTPUT, 'w', encoding='utf8') as wf:
    with codecs.open(INPUT, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip().split(' ')
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
