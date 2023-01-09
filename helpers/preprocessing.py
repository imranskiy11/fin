import numpy as np
from datetime import datetime

def shift_sequence(seq: np.array) -> np.array:
    ''' shift sequence '''
    return seq[:-1] - seq[1:]
    
def divide_numdate(num_date):
    return f'{num_date[0:4]}:{num_date[4:6]}:{num_date[6:8]}'

def divide_timedate(time_date, pairs_count=3):
    time_date = (6 - len(time_date))*'0' + time_date
    time_date = ':'.join([time_date[2*i:2*(i+1)] for i in range(pairs_count)])
    return time_date

def to_datetime_index_date(index_date, pattern='%Y:%m:%d %H:%M:%S'):
    return datetime.strptime(index_date, pattern)