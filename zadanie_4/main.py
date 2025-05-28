import numpy as np
from pymcdm.methods import TOPSIS, SPOTIS
from pymcdm.normalizations import MinMaxNormalization

# Dane
matrix = np.array([[250, 16, 12], [200, 20, 8], [300, 14, 10]])
weights = np.array([0.5, 0.3, 0.2])
criteria_types = ['min', 'max', 'min']

# Normalizacja
normalizer = MinMaxNormalization()
norm_matrix = normalizer.normalize(matrix, criteria_types)

# Metody
topsis = TOPSIS()
spotis = SPOTIS()

topsis_scores = topsis(norm_matrix, weights, criteria_types)
spotis_scores = spotis(norm_matrix, weights, criteria_types)

print('TOPSIS:', topsis_scores)
print('SPOTIS:', spotis_scores)
