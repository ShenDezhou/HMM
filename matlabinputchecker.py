import codecs

with codecs.open('pku_train_states.txt', 'r', encoding='utf8') as wfa:
    states = wfa.readlines()
    with codecs.open('pku_train_vec_seq.txt', 'r', encoding='utf8') as wfb:
        seqs = wfb.readlines()
        for i in range(len(states)):
            if len(states[i]) != len(seqs[i].split(",")):
                print(i)
    print('FIN')
