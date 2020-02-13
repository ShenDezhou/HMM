import codecs

from testing.neglogviterbi import neglogviterbi

MODE = 4

if MODE == 1:
    INPUT = '../plain/pku_training.utf8'
    OUTPUT = '../state/hmm/pku_train_hmmstate.utf8'

if MODE == 2:
    INPUT = '../plain/pku_test.utf8'
    OUTPUT = '../state/hmm/pku_test_hmmstate.utf8'

if MODE == 3:
    INPUT = '../plain/pku_training_words.utf8'
    OUTPUT = '../state/hmm/pku_train_words_hmmstate.utf8'

if MODE == 4:
    INPUT = '../plain/pku_test_words.utf8'
    OUTPUT = '../state/hmm/pku_test_words_hmmstate.utf8'

statenames = "BMES"
with codecs.open(OUTPUT, 'w', encoding='utf8') as wf:
    with codecs.open(INPUT, 'r', encoding='utf8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace(" ", "").strip()
            if len(line) == 0:
                wf.write('\n')
                continue
            bestpath, bestpathprob = neglogviterbi(line)
            for w in bestpath:
                wf.write(statenames[w])
            wf.write('\n')
    print("FIN")
