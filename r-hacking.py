import csv
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt

f = open("organizeyourmusic_formatted.csv", 'r')
csvReader = csv.DictReader(f)

#title,artist,top genre,year,added,bpm,nrgy,dnce,dB,live,val,dur,acous,spch,pop
unique_pairs = list(combinations(csvReader.fieldnames[5:], 2))
correlation_list = []
for p0, p1 in unique_pairs:
    f = open("organizeyourmusic_formatted.csv", 'r')
    csvReader = csv.DictReader(f)
    data0, data1 = [], []
    for col in csvReader:
        data0.append(int(col[p0]))
        data1.append(int(col[p1]))
    correlation = np.corrcoef(data0, data1)
    correlation_list.append([correlation[0][1], p0, data0, p1, data1])

ar = np.arange(45)
plt.bar(ar, [e[0] for e in correlation_list])
plt.xlabel('Data pairs')
plt.ylabel('Pearson correlation coefficient')
plt.title('Correlation')
plt.grid(True)
plt.legend()
plt.show()

index_min = np.argmin([e[0] for e in correlation_list])
index_max = np.argmax([e[0] for e in correlation_list])
plt.plot(np.arange(39), correlation_list[index_max][2], label = correlation_list[index_max][1])
plt.plot(np.arange(39), correlation_list[index_max][4], label = correlation_list[index_max][3])

plt.xlabel('Data')
plt.ylabel('Magnitude')
plt.title('Max positive correlation')
plt.grid(True)
plt.legend()
plt.show()


plt.plot(np.arange(39), correlation_list[index_min][2], label = correlation_list[index_min][1])
plt.plot(np.arange(39), correlation_list[index_min][4], label = correlation_list[index_min][3])

plt.xlabel('Data')
plt.ylabel('Magnitude')
plt.title('Max negative correlation')
plt.grid(True)
plt.legend()
plt.show()
