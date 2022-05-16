import numpy as np
import pandas as pd
def import_from_file(filename: str) -> np.ndarray:
    df = pd.read_csv(filename)
    sequence = int(np.max(df['Sequence']) + 1)
    retval = []
    for seq in range(sequence):
        data = df[df['Sequence'] == seq].mean()
        retval.append(data.to_numpy())
    
    return np.array(retval)