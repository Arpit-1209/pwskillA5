import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(25)
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
}
df = pd.DataFrame(data)

plt.scatter(df['GDP'], df['Population'], s=df['Population']*10, alpha=0.5)
for i, txt in enumerate(df['Country']):
    plt.annotate(txt, (df['GDP'][i], df['Population'][i]))
plt.xlabel('GDP')
plt.ylabel('Population')
plt.title('Bubble Chart')
plt.show()
