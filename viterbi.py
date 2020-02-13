import codecs

import numpy
from scipy.io import loadmat

te = loadmat('matlab/te.mat')
t = te['t']
e = te['e']
print(e)
chars = []
dicts = {}

with codecs.open('pku_dic/pku_dict.utf8', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        for w in line:
            chars.append(w)
print(len(chars))
dicts = dict(zip(chars, range(0, len(chars))))
print(len(dicts))
a_seq = '我来到北京清华大学'
T = len(a_seq)
N = len("BMES")
print(N, T)
viterbi = numpy.zeros((N, T))
backpointer = numpy.zeros((N, T), dtype=int)
start_p = [0.5, 0, 0, 0.5]  # BMES

for i_state in range(N):
    viterbi[i_state, 0] = e[i_state, dicts[a_seq[0]]] * start_p[i_state]
    backpointer[i_state, 0] = 0
print(viterbi[:, 0], backpointer[:, 0])
for i_seq in range(1, T):
    print(a_seq[i_seq])
    for i_state in range(N):
        viterbi[i_state, i_seq] = max(
            viterbi[:, i_seq - 1] * numpy.transpose(t[:, i_state]) * e[:, dicts[a_seq[i_seq]]])
        backpointer[i_state, i_seq] = numpy.argmax(
            viterbi[:, i_seq - 1] * numpy.transpose(t[:, i_state]) * e[:, dicts[a_seq[i_seq]]], axis=0)
        print(viterbi[i_state, i_seq], backpointer[i_state, i_seq])
    print(viterbi[:, i_seq], backpointer[:, i_seq])
bestpathprob = numpy.max(viterbi[:, -1])
bestpathpointer = numpy.argmax(viterbi[:, -1])
bestpath = []
print(bestpathprob, bestpathpointer)
for r_seq in range(T - 1, -1, -1):
    bestpath.append(bestpathpointer)
    print(r_seq, bestpath)
    bestpathpointer = backpointer[bestpathpointer, r_seq]
bestpath.reverse()
print(bestpath, bestpathprob)
