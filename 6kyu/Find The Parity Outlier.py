import numpy as np
def find_outlier(integers):
    integers_np = np.array(integers)
    mask = integers_np % 2 == 0
    return integers_np[~mask].item() if sum(mask)>1 else integers_np[mask].item()