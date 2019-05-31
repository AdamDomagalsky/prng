
# %matplotlib inline
from wichmann_hill import Wichmann_Hill
from lehmer import Lehmer
from invwk import Invwk
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats

def ith_experiment(scope=20, times=100):
    # generator = Lehmer(scope=scope)
    generator = Invwk(scope=scope)
    # generator = Wichmann_Hill(scope=scope)

    return np.array([ generator.get_random() for _ in range(times)])

N=100

iths_arr = [ith_experiment() for _ in range(N)]


means = np.array([arr.mean() for arr in iths_arr])
stds = np.array([arr.std() for arr in iths_arr])
var = np.array([arr.var() for arr in iths_arr])
print(element for element in iths_arr)

sns.distplot(means)
plt.show()

sns.distplot(stds)
plt.show()

sns.distplot(var)
plt.show()

#
# ts = stats.t(np.array(iths_arr))
# print(ts)
iqr = stats.iqr(np.array(iths_arr))
print(iqr)




