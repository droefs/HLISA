import numpy as np
import random
import matplotlib.pyplot as plt

NEG_SCALE = -10
SCALE = 300
N = 10000

MEAN = 100
STD = 33
MINIMAL = 90

def std_positive(mean, std, minimal):
    if minimal > mean:
        raise Exception('minimal must be lower then mean')
    sample = np.random.normal(mean, std)
    if sample < minimal:
        sample += (minimal-sample) + (mean - minimal)*random.random()
        sample += (minimal-sample) + ((((mean - minimal) + (1/3) * std)**0.5)*random.random())**2
        # sample += (minimal-sample) + (3.333*std)*random.random()
        # sample += (minimal-sample) + (3.33333*std)*random.random()**1.5
        # sample += (minimal-sample) + (3.3333333*std)*np.random.normal(0.5, 0.3333333)
        # sample += (minimal-sample) + (((random.random()*(1.5**0.5))**2)*((3*std)/2)*random.random())
        # sample += (minimal-sample) + (3.333*std+(minimal-sample)/2)*random.random()
        # sample += (minimal-sample) + (3.333*std)*np.random.normal(mean+(std/2), std/6)
        
    return sample

counts = {i: 0 for i in range(NEG_SCALE, SCALE)}
for i in range(N): 
    counts[int(std_positive(MEAN, STD, MINIMAL))] += 1
y = [counts[i] for i in range(NEG_SCALE, SCALE)]
x = [i for i in range(NEG_SCALE, SCALE)] 

colors = [i for i in range(SCALE-NEG_SCALE)]
plt.scatter(x, y, c=colors, alpha=0.5)
plt.title(f"Distrubution of std_positive, N={N} mean={MEAN}, std={STD}, min={MINIMAL}")
plt.xlabel("rounded std_positive value")
plt.ylabel("count")
plt.show()