import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = np.random.rand(10, 10)
correlation_matrix = np.corrcoef(data)

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

