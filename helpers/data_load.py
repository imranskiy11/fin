import pandas as pd
from typing import List

def load_data_from_txt(path: str, sep: str='\t', skipinitialspace: bool=True, header: bool=None, 
    names: List[str]=['EURUSD', 'num' 'date', 'time', 'open', 'max', 'min', 'close', 'vol']
    ) -> pd.DataFrame:
    
    """
    Load data from txt file
    """
    
    return pd.read_csv(
        path, sep=sep, skipinitialspace=skipinitialspace, 
        header=header, names=names)
        
        


if __name__ == '__main__':
    print()