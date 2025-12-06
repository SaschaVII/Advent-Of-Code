from math import prod; from itertools import groupby
l=open('inputTest.txt').read().splitlines()
print(sum((sum(a) if b=='+' else prod(a)) for b,a in zip(l.pop().split(), [[int(''.join(c)) for c in g] for k,g in groupby(zip(*l), lambda c: set(c)=={' '}) if not k])))