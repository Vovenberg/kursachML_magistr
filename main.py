from Yakobi import Yakobi
import numpy as np
import pylab as pl


def runYakobi():
    k = np.random.randint(5, 15)
    gamma = np.random.random_integers(1, 20, 15)
    betta = np.random.random_integers(1, 20, 15)
    resultN = Yakobi().processN(gamma, betta, k)
    print(f'Step: {k}')
    print(f'Gamma: {gamma}')
    print(f'Betta: {betta}')
    print(f'Res N: {resultN}')
    plotStepsN(range(0, k), resultN)

def plotStepsN(steps, n):
    pl.plot(steps, n, color ='red')
    pl.xlabel('Steps')
    pl.ylabel('N')
    pl.savefig('yakobi.png')
    pl.show()

runYakobi()
