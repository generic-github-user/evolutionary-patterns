import numpy as np
import matplotlib.pyplot as plt
import random

width = 100
height = 100

base = np.random.uniform(0, 1, [width, height, 1])
base = np.zeros([width, height, 1])
for i, y in enumerate(base):
    for j, x in enumerate(y):
        base[i][j] = i+j
# base = np.ones([30, 30, 1])
