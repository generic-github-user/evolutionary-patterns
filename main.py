import numpy as np
import matplotlib.pyplot as plt
import random

width = 100
height = 100
bases_per_axis = 15
noise = (-0.05, 0.05)
num_filters = 8
samples = (3, 3)
base_range = (-1, 1)
filter_range = (-10, 10)
total_filters = bases_per_axis * num_filters
total_ops = total_filters * width * height
print(total_filters, total_ops)

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


x = np.linspace(*base_range, width)
y = np.linspace(*base_range, height)
bases = []
for i in range(bases_per_axis):
    for r in np.meshgrid(x, y):
        bases.append(r + np.random.uniform(*noise, [width, height]))

print([b.shape for b in bases])

# https://codereview.stackexchange.com/a/185794
def norm(array):
    return np.interp(array, (array.min(), array.max()), (-1, +1))

filters = []
filter_types = [
    [np.sin],
    [np.cos],
    # [np.square],
    [np.add, filter_range],
    [np.multiply, filter_range],
    [norm]
    # # [np.reciprocal],
    # [np.negative],
    # [np.positive],
    # [np.mod, (-5, 5)]
    # [np.power, (1, 3)]
    # [np.sqrt]
]
def filter_wrapper(ft):
    # print(ft)
    def filter_func(filter_input):
        if len(ft) > 1:
            args = [np.random.uniform(*b) for b in ft[1:]]
            # print(ft[1:])
            return ft[0](filter_input, *args)
        else:
            return ft[0](filter_input)
    return filter_func

for b in range(len(bases)):
    bf = []
    for i in range(num_filters):
        f = filter_wrapper(random.choice(filter_types))
        bf.append(f)
    filters.append(bf)

print(filters[0])

def generate():
    results = []
    for i, b in enumerate(bases):
        g = b
        for f in filters[i]:
            g = f(g)
        results.append(g)
    result = np.product(np.stack(results), axis=0)
    return result

# print([r.shape for r in results])
# print(result.shape)
# print(np.stack(results).shape)
# print(results)

# plt.imshow(result, cmap='plasma')
# plt.show()

generated = []
for m in range(np.prod(samples)):
    generated.append(generate())

fig, ax = plt.subplots(*samples)
# ax4.plot(x, -y**2, 'tab:red')
print(generated)

index = 0
for iy in ax:
    for ix in iy:
        ix.imshow(generated[index], cmap='plasma')
        index += 1

for ax in fig.get_axes():
    ax.label_outer()

plt.show()
