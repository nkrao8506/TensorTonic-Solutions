import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    nmp_x = np.array(x)
    return 1/(1 + np.exp(-nmp_x))