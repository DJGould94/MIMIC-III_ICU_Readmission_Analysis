import pandas as pd
import os

def dataframe_from_csv(path):
    if os.path.exists(path+".gz"):
        path = path + ".gz"

    return pd.read_csv(path)
