import matplotlib.pyplot as plt
data = [3, 7, 9, 15, 22, 29, 35]

plt.hist(data, bins=5)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
