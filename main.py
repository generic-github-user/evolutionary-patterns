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


# bases = [
#     np.linspace([0,0],[1,0],num=width,axis=0),
#     np.linspace([0,0],[0,1],num=height,axis=1)
# ]

bases_per_axis = 2
x = np.linspace(0, 1, width)
y = np.linspace(0, 1, height)
bases = []
for i in range(bases_per_axis):
    for r in np.meshgrid(x, y):
        bases.append(r + np.random.uniform(0, 0.1, [width, height]))

print([b.shape for b in bases])

filters = []
filter_types = [
    [np.sin],
    [np.cos],
    [np.square],
    [np.add, (-5, 5)],
    [np.multiply, (-5, 5)],
    # [np.reciprocal],
    [np.negative],
    [np.positive],
    # [np.power, (1, 3)]
    # [np.sqrt]
]
def filter_wrapper(ft):
    print(ft)
    def filter_func(filter_input):
        if len(ft) > 1:
            args = [np.random.uniform(*b) for b in ft[1:]]
            print(ft[1:])
            return ft[0](filter_input, *args)
        else:
            return ft[0](filter_input)
    return filter_func
