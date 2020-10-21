from operator import itemgetter
from itertools import groupby
""" note  the sorting element in the print. using int(k) and len(list(g)) I messed this up earlier
maybe explore other ways to use groupby in different scenarios """

data = input()
for k, g in groupby(data):
    print((len(list(g)),int(k)), end=' ') # think about each part and what to do to generate the output
