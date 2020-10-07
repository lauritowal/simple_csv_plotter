import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('file.txt','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(float(row[0].strip()))
        y.append(float(row[1].strip()))

plt.plot(x, y, color='blue', marker='o', linestyle='dashed', linewidth=2, markersize=12, markerfacecolor="red")

plt.xlabel('x')
plt.ylabel('y')
plt.title('Weg')
plt.legend()
plt.show()