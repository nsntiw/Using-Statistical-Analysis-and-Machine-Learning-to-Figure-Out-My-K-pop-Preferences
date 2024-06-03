import csv
from itertools import combinations
import numpy as np
import matplotlib.pyplot as plt
import math

f = open("3_top100_formatted.csv", 'r')
csvReader = csv.DictReader(f)

#title,artist,top genre,year,added,bpm,nrgy,dnce,dB,live,val,dur,acous,spch,pop
#nrgy = energy, dnce = danceability, val = valence, dur = duration, acous = acousticness, spch = speechiness, pop = popularity
for i in csvReader.fieldnames[5:]:
    f = open("3_top100_formatted.csv", 'r')
    csvReader = csv.DictReader(f)
    data = []
    for col in csvReader:
        data.append(int(col[i]))
    plt.hist(data, 15)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(f"{i}")
    plt.grid(True)
    plt.show()

unique_pairs = list(combinations(csvReader.fieldnames[5:], 2))
correlation_list = []
for p0, p1 in unique_pairs:
    f = open("3_top100_formatted.csv", 'r')
    csvReader = csv.DictReader(f)
    data0, data1 = [], []
    for col in csvReader:
        data0.append(int(col[p0]))
        data1.append(int(col[p1]))
    correlation = np.corrcoef(data0, data1)
    correlation_list.append([correlation[0][1], p0, data0, p1, data1])

plt.bar(np.arange(45), [e[0] for e in correlation_list])
plt.xlabel('Data pairs')
plt.ylabel('Pearson correlation coefficient')
plt.title('Correlation')
plt.grid(True)
plt.legend()
plt.show()


for e in (np.absolute([e[0] for e in correlation_list]).argsort() [::-1]):
    if(abs(correlation_list[e][0]) < 0.5):
        break
    data0 = correlation_list[e][2]
    data1 = correlation_list[e][4]
    data0_normalised = [(e - min(data0)) / (max(data0) - min(data0)) for e in data0]
    data1_normalised = [(e - min(data1)) / (max(data1) - min(data1)) for e in data1]
    plt.plot(np.arange(len(data0_normalised)), data0_normalised, color = "red", label = correlation_list[e][1])
    plt.plot(np.arange(len(data0_normalised)), data1_normalised, color = "blue",label = correlation_list[e][3])
    
    coeffs = np.polyfit(np.arange(len(data0_normalised)), data0_normalised, 4)
    p = np.poly1d(coeffs)
    plt.plot(np.arange(39), p(np.arange(39)))
    coeffs = np.polyfit(np.arange(len(data0_normalised)), data1_normalised, 4)
    p = np.poly1d(coeffs)
    plt.plot(np.arange(len(data0_normalised)), p(np.arange(len(data0_normalised))))
    

    plt.xlabel('Data')
    plt.ylabel('Magnitude')
    plt.title(f"Correlation: {correlation_list[e][0]}")
    plt.grid(True)
    plt.legend()
    plt.show()
