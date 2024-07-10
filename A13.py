import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(20)
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)
pivot_table = df.pivot('Day', 'Month', 'Sales')

sns.heatmap(pivot_table, annot=True, fmt="d", cmap='YlGnBu')
plt.title('Sales Heatmap')
plt.show()
