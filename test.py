import csv
import numpy as np
import torch

data_path = ""

ds = np.loadtxt(data_path,dtype=np.float, delimiter = ',',skiprows=1)

print(ds)

col = next(csv.reader(open(data_path), delimiter = ';'))
print(col)


py_ds = torch.from_numpy(ds)

print(py_ds,py_ds.shape,py_ds.dtype)