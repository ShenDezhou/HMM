import codecs

import numpy
from scipy.io import loadmat

# Take log so that using plus to replace multiplication to avoid decimal underflow
te = loadmat('matlab/te.mat')
t = te['t']
t[t == 0] = 1e-200
e = te['e']
print(t)
chars = []
dicts = {}

with codecs.open('pku_dic/pku_dict.utf8', 'r', encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        for w in line:
            chars.append(w)
print(len(chars))
dicts = dict(zip(chars, range(len(chars))))
print(len(dicts))
a_seq = '法律法规'
T = len(a_seq)
N = len("BMES")
print(N, T)
viterbi = numpy.zeros((N, T))
backpointer = numpy.zeros((N, T), dtype=int)
start_p = [0.5, 1e-200, 1e-200, 0.5]  # BMES

for i_state in range(N):
    viterbi[i_state, 0] = -numpy.log(e[i_state, dicts[a_seq[0]]]) - numpy.log(start_p[i_state])
    backpointer[i_state, 0] = 0
print(viterbi[:, 0], backpointer[:, 0])
for i_seq in range(1, T):
    print(a_seq[i_seq])
    for i_state in range(N):
        viterbi[i_state, i_seq] = min(
            viterbi[:, i_seq - 1] - numpy.log(t[:, i_state]) - numpy.log(e[:, dicts[a_seq[i_seq]]]))
        backpointer[i_state, i_seq] = numpy.argmin(
            viterbi[:, i_seq - 1] - numpy.log(t[:, i_state]) - numpy.log(e[:, dicts[a_seq[i_seq]]]), axis=0)
        print(viterbi[i_state, i_seq], backpointer[i_state, i_seq])
    print(viterbi[:, i_seq], backpointer[:, i_seq])
bestpathprob = numpy.min(viterbi[:, -1])
bestpathpointer = numpy.argmin(viterbi[:, -1])
bestpath = []
print(bestpathprob, bestpathpointer)
for r_seq in range(T - 1, -1, -1):
    bestpath.append(bestpathpointer)
    print(r_seq, bestpath)
    bestpathpointer = backpointer[bestpathpointer, r_seq]
bestpath.reverse()
print(bestpath, bestpathprob)
