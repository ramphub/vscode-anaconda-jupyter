import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
#%%
x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show() 

#%%
import pandas as pd
s = pd.Series([1,3,5,np.nan,6,8])
s.shape
