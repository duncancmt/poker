import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(__file__), "stupid_python_tricks"))

from polynomial import *
from horner import *
import cPickle as pickle

A = 486662
#               c  Px Pz Qx Qy Qz Rx Rz
numerator = [[   2, 3, 2, 2, 1, 1, 0, 1],
             [ 2*A, 2, 3, 2, 1, 1, 0, 1],
             [   2, 1, 4, 2, 1, 1, 0, 1],
             [  -4, 4, 1, 1, 1, 2, 0, 1],
             [-4*A, 3, 2, 1, 1, 2, 0, 1],
             [  -4, 2, 3, 1, 1, 2, 0, 1],
             [   2, 5, 0, 0, 1, 3, 0, 1],
             [ 2*A, 4, 1, 0, 1, 3, 0, 1],
             [   2, 3, 2, 0, 1, 3, 0, 1]]




#                 c  Px Pz Qx Qy Qz Rx Rz
denominator = [[  -1, 0, 5, 0, 0, 4, 1, 0],
               [   1, 0, 5, 2, 2, 0, 0, 1],
               [  -2, 1, 4, 1, 2, 1, 0, 1],
               [   1, 3, 2, 2, 0, 2, 0, 1],
               [   A, 2, 3, 2, 0, 2, 0, 1],
               [   1, 1, 4, 2, 0, 2, 0, 1],
               [   1, 2, 3, 0, 2, 2, 0, 1],
               [  -2, 4, 1, 1, 0, 3, 0, 1],
               [-2*A, 3, 2, 1, 0, 3, 0, 1],
               [  -2, 2, 3, 1, 0, 3, 0, 1],
               [  -1, 0, 5, 1, 0, 3, 0, 1],
               [   1, 5, 0, 0, 0, 4, 0, 1],
               [   A, 4, 1, 0, 0, 4, 0, 1],
               [   1, 3, 2, 0, 0, 4, 0, 1],
               [  -1, 1, 4, 0, 0, 4, 0, 1],
               [  -A, 0, 5, 0, 0, 4, 0, 1]]

vars = ['Px', 'Pz', 'Qx', 'Qy', 'Qz', 'Rx', 'Rz']

n = Polynomial()
for term_info in numerator:
    term = Term(term_info[0])
    for i, power in enumerate(term_info[1:]):
        term *= Term((vars[i], power))
    n += term

d = Polynomial()
for term_info in denominator:
    term = Term(term_info[0])
    for i, power in enumerate(term_info[1:]):
        term *= Term((vars[i], power))
    d += term

def monitor(*args):
    print args[0], args[1:]

n_ops = horner_form_tmp(n, None, monitor)
f = open("sum_verification_polynomial_numerator.pkl","wb")
p = pickle.Pickler(f, -1)
p.dump(n_ops)
del p
f.flush()
f.close()
del f

d_ops = horner_form_tmp(d, None, monitor)
f = open("sum_verification_polynomial_denominator.pkl","wb")
p = pickle.Pickler(f, -1)
p.dump(d_ops)
del p
f.flush()
f.close()
del f
