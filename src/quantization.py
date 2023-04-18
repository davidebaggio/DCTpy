from importModules import *


def quantization_of_matrixprev(dct_values, thresh):
    per = np.percentile(abs(dct_values), thresh)
    return dct_values * (abs(dct_values) >= per)


def quantization_of_matrix(dct_values, thresh):
    thresh = thresh / 100
    return dct_values * (abs(dct_values) > (thresh * np.max(dct_values)))