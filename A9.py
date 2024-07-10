import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

data = {'Category': ['A', 'B', 'C', 'D', 'E'] * 20,
        'Value': np.random.randint(1, 100, 100)}

df = pd.DataFrame(data)
sns.boxplot(x='Category', y='Value', data=df)
plt.title('Box Plot')
plt.show()
