# -*- coding: utf-8 -*-
import sys
from random import randint
# from string import maketrans
print(ord("i"))
crypted = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
oplossing = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'

strin = ''
dddd = ''
ver = ''
fff = []
gggg = []
for letter in crypted:
    fff.append(ord(letter))

for letter in oplossing:
    gggg.append(ord(letter))

for ff in fff:
    dddd += str(gggg[fff.index(ff)]) + ' '
    strin += str(ff) + ' '
    nu = gggg[fff.index(ff)] + ff
    ver += str(nu) + ' '

print(strin)
print(dddd)
print(ver)

