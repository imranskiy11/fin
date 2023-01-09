import numpy as np
from datetime import datetime

def shift_sequence(seq: np.array) -> np.array:
    """ shift sequence """
    return seq[:-1] - seq[1:]
    
def divide_numdate(num_date):
    """ 
    divide numdate column
    from 20201005 to 2020:10:05
    """
    return f'{num_date[0:4]}:{num_date[4:6]}:{num_date[6:8]}'

def divide_timedate(time_date, pairs_count=3):
    """
    divide time_date column
    from '500' to '00:05:00'
    """
    time_date = (6 - len(time_date))*'0' + time_date
    time_date = ':'.join([time_date[2*i:2*(i+1)] for i in range(pairs_count)])
    return time_date

def to_datetime_index_date(index_date, pattern='%Y:%m:%d %H:%M:%S'):
    return datetime.strptime(index_date, pattern)
    
    
def prep_dataframe(dataframe, inplace=False):
    """
    preprocessing default dataframe for indexing by datetime type
    """
    
    if not inplace:
        df = dataframe.copy(deep=True)
    else:
        df = dataframe
     
    df.numdate = df.numdate.astype(str)
    df.time = df.time.astype(str)
    
    df['hms'] = df.time.apply(divide_timedate)
    df['ymd'] = df.numdate.apply(divide_numdate)
    
    df['index_date'] = df.ymd + ' ' + df.hms
    df.index_date.apply(to_datetime_index_date)
    
    df.drop(['ymd', 'hms', 'EURUSD', 'numdate', 'time'], axis=1, inplace=True)
    
    df.set_index('index_date', inplace=True
    return df