import pandas as pd
import os

def dataframe_from_csv(path, header=0, index_col=0):
    if os.path.exists(path+".gz"):
        path = path + ".gz"

    return pd.read_csv(path, header=header, index_col=index_col)
