import codecs

MODE = 2

if MODE == 1:
    # train
    GOLD = '../state/gold/pku_train_states.txt'
    HMM = '../state/hmm/pku_train_hmmstate.utf8'
    # sentence correct: 0.012437027707808565
    # character error: 0.8500198576664421
    # novel:
    # sentence correct: 0.00530016792611251
    # character error: 0.7386382118993535

if MODE == 2:
    # test
    GOLD = '../state/gold/pku_test_states.txt'
    HMM = '../state/hmm/pku_test_hmmstate.utf8'
    # sentence correct: 0.00205761316872428
    # character error: 0.8554424258037319
    # novel:
    # sentence correct: 0.00720164609053498
    # character error: 0.7407869240181012

if MODE == 3:
    # train words
    GOLD = '../state/gold/pku_train_words_states.txt'
    HMM = '../state/hmm/pku_train_words_hmmstate.utf8'
    # sentence correct: 0.600853479919715
    # character error: 0.1678944986422609

if MODE == 4:
    # test words
    GOLD = '../state/gold/pku_test_words_states.txt'
    HMM = '../state/hmm/pku_test_words_hmmstate.utf8'
    # sentence correct: 0.6512017036811683
    # character error: 0.1263151690194807

with codecs.open(GOLD, 'r', encoding='utf8') as wfa:
    states = wfa.readlines()
    with codecs.open(HMM, 'r', encoding='utf8') as wfb:
        seqs = wfb.readlines()
        for i in range(len(states)):
            if len(states[i]) != len(seqs[i]):
                print(i)
    print('FIN')

sentence = 0
e_character = 0
t_character = 0
with codecs.open(GOLD, 'r', encoding='utf8') as wfa:
    states = wfa.readlines()
    sentence = len(states)
    with codecs.open(HMM, 'r', encoding='utf8') as wfb:
        seqs = wfb.readlines()
        for i in range(len(states)):
            if states[i] != seqs[i]:
                sentence -= 1
                print(i)
                for ii in range(len(states[i]) - 2):
                    t_character += 1
                    if states[i][ii] != seqs[i][ii]:
                        e_character += 1
            else:
                t_character += len(states[i])
                print('correct index:', i)
    print('sentence correct:', float(sentence) / len(states))
    print('character error:', float(e_character) / t_character)
    print('FIN')
