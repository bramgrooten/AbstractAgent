import numpy as np

with open("best_param_200.npy", "rb") as file:
    param = np.load(file)
print(param)