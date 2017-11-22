import numpy as np
import pylab as pl

from jacobi.calculate import Jacobi


def runJacobiWithRandomArgs():
    k = 100
    gamma = np.random.random_integers(1, 20, 100)
    betta = np.random.random_integers(1, 20, 100)
    jacobi = Jacobi()
    resultN = jacobi.processN(gamma, betta, k)
    resultN0 = jacobi.processN0(gamma, betta)
    resultN1 = jacobi.processN1(gamma, betta)
    print(f'Step: {k}')
    print(f'Gamma: {gamma}')
    print(f'Betta: {betta}')
    print(f'Res N: {resultN}')
    print(f'Res N0 {resultN0}')
    print(f'Res N1 {resultN1}')
    plotStepsN(range(0, k), resultN)

def plotStepsN(steps, n, filename = 'jacobi_plot.png'):
    pl.plot(steps, n, color ='red')
    pl.xlabel('Steps')
    pl.ylabel('N')
    pl.savefig(filename)
    pl.show()

runJacobiWithRandomArgs()
