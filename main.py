from Yakobi import Yakobi
import numpy as np

k = np.random.randint(1, 10)
gamma = np.random.random_integers(1, 20, 10)
betta = np.random.random_integers(1, 20, 10)
resultN = Yakobi().processN(gamma, np.random.random_integers(1, 20, 10), k)
print(f'Step: {k}')
print(f'Gamma: {gamma}')
print(f'Betta: {betta}')
print(f'Res N: {resultN}')
