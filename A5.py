import matplotlib.pyplot as plt
sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

plt.pie(sizes, labels=sections, autopct='%1.1f%%')
plt.title('Pie Chart')
plt.show()
