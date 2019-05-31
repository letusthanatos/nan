#!/usr/bin/python3

import pickle
import pandas as pd
import sys
xr = sys.argv[1].split(',')
f = [4,5,22,24,26]
xr = [float(xr[i]) for i in f]

loaded_model = pickle.load(open("model_pickle (1)", 'rb'))

result = loaded_model.predict([xr])

print(result[0],end="")