import numpy as np
import scipy.stats as ss
n = np.array([1] * 89 + [0] * 11)
p0 = 0.85
p = n.mean()
s = n.std()
z = (p - p0) / (np.sqrt(p0 * (1 - p0) / 100))
if 1 - ss.norm(0,1).cdf(z) < 0.05:
  print("Нейросеть лучше")
print("Нейросеть НЕ лучше")