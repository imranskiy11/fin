import pandas as pd
import numpy as np

def get_sequence(
    df: pd.DataFrame, col_name: str='open', 
    start_point: int=0, end_point: int=100)-> np.array:
    
    """ Get pandas series slice from current dataframe"""
    
    return df[col_name][start_point:end_point].values

if __name__ == '__main__':
    print()