import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

from mpl_toolkits.mplot3d import Axes3D

np.random.seed(30)
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data['X'], data['Y'], data['Z'])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('3D Scatter Plot')
plt.show()
