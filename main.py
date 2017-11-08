import math as m
import cmath as cm
import numpy as np

c = 2
k = range(0, 10)
w = complex(1, 2)
j = complex(1, 5)


def funcV(gamma, betta):
    return _funcV_(gamma, betta, wj_func_with_phase())


def funcV_rem(gamma, betta):
    return _funcV_(gamma, betta, wj_func_with_w_only())


# //////////////

def _funcV_(gamma, betta, wj_func):
    return list(map(lambda ki: main_func(ki, gamma[ki], betta[ki], wj_func), k))


def main_func(ki, gamma, betta, wj_func):
    p = range(1, betta)
    res1_0 = 1
    for pi in p:
        res1_0 *= ((2 * ki + 2 * pi + 1) * c * gamma / 2) + wj_func
    res1 = pow(pow(c, 2), betta + 1) * (2 * ki + betta + 1) * (m.factorial(betta + ki)) / m.factorial(ki) * res1_0

    res2 = 0
    for si in range(0, ki):
        res_inter_1 = m.factorial(ki) / m.factorial(si) * (ki - si)
        res_inter_2 = pow(m.factorial((ki + si)) / m.factorial(si) * m.factorial(ki), -1)
        res_inter_3 = 1 / (((2 * si + 1) * c * gamma / 2) + wj_func)
        res2 += res_inter_1 * res_inter_2 * res_inter_3
    return res1 * res2


# /////////////////
def wj_func_with_phase():
    return (cm.phase(w) * cm.phase(j))


def wj_func_with_w_only():
    return cm.phase(w)


# ////////////////

def findDelta(gamma, betta):
    resV = funcV(gamma, betta)
    return list(map(lambda resV1, b1: m.sqrt((8 * b1) / m.fabs(resV1)), resV, betta))


def findMax(gamma, betta):
    resV = funcV_rem(gamma, betta)
    conditionArray1 = list(filter(lambda i: 2 < i < 10, resV))
    conditionArray2 = list(filter(lambda i: -7 < i < 3, resV))
    return max([max(conditionArray1), max(conditionArray2)])


# invoke this
def processN(gamma, betta):
    delta = findDelta(gamma, betta)
    max = findMax(gamma, betta)
    return list(map(lambda delta: max / delta + 0.5, delta))


print(processN(np.random.random_integers(1, 20, 10), np.random.random_integers(1, 20, 10)))
