import numpy

seq = [165, 170, 165, 175, 155, 165, 165, 150, 155, 160, 160, 165, 170, 165, 170]
N = len(seq)
dic = {}
dic[150] = 0
dic[155] = 1
dic[160] = 2
dic[165] = 3
dic[170] = 4
dic[175] = 5
rdic = dict(zip(dic.values(), dic.keys()))
nstate = len(set(seq))
t = numpy.zeros((nstate, nstate))
for i in range(len(seq) - 1):
    t[dic[seq[i]], dic[seq[i + 1]]] = 1

print(t)
for i in range(nstate):
    s = sum(t[i, :])
    t[i, :] = t[i, :] / s

print(t)
p0 = numpy.array([0, 0, 0, 1, 0, 0])

r = p0
for i in range(N):
    p = numpy.zeros((1, nstate))
    p[0, dic[seq[i]]] = 1
    print('start p:', p)
    for j in range(N - i):
        p = p * t
    print('Prediction of Year 2020 from ' + str(2005 + i) + ' is: y=p0*p^' + str(N - i))
    x = numpy.argmax(p)
    a = x // nstate
    b = x % nstate
    print('Prediction of Year 2020 from ' + str(2005 + i) + ' result score is:' + str(rdic[b]))
