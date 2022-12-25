import numpy as np

def shift_sequence(seq: np.array) -> np.array:
    ''' shift sequence '''
    return seq[:-1] - seq[1:]