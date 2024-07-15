import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from scipy import odr

ranking = ['ASAP','Sorry',"She's in the Rain",'Like We Used To','MANIAC','Miniskirt',
           'WANNA BE MYSELF','DM','MAMA - Chinese Version','Like Ooh-Ahh','Likey','The Feels','SCIENTIST','FANCY','SO BAD','Back to the City','Baddie','Illusion','Drama',
           'Give it to me','MAGO','Congratulations','What is Love','Mr-Ambiguous',
           "You're the Best","I CAN'T STOP ME",'Talk that Talk','To. X','OMG','Home',
           'Shooting Star','Ditto','Alcohol-Free','Rough','Love 119','LEFT RIGHT','Magnetic',
           'YES or YES','Feel Special','Heart Shaker','TT','CRY FOR ME','CHEER UP','Black Mamba'
           ,'Next Level','Time of Our Life','Super Shy','SET ME FREE','Knock Knock',
           'MOONLIGHT SUNRISE','Get A Guitar','Basics','History - Chinese Version',
           'LOVE ME RIGHT - Chinese Version','Monster - Chinese Version','Spicy','MORE & MORE']
ranked_data_list = []


with open("Data/3_myplaylist_formatted.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    csv_data = list(reader) 

while ranking:
    track = ranking.pop(0)
    for row in csv_data:
        if (row['title']) == track:
            ranked_data_list.append(row)
#print(ranked_data_list)

#bpm,nrgy,dnce,dB,live,val,dur,acous,spch,pop
#convert bpm figure from string to int such that it will be plotted from lowest to highest on y
for data_type in ['bpm','nrgy','dnce','dB','live','val','dur','acous','spch','pop']:
    #scatter plot
    x = range(len(ranked_data_list))
    y = [int(e[data_type]) for e in ranked_data_list]
    plt.scatter(x, y)
    #regression and calculate r, p
    linear_regression = np.poly1d(np.polyfit(x, y, 1))(x)
    quadratic_regression = np.poly1d(np.polyfit(x, y, 2))(x)
    r, p = pearsonr(x, y)
    r2 = r**2
    plt.plot(x, linear_regression, color = 'red', label = f"r = {r:.3f}, r2 = {r2:.3f}, p = {p:.3f}")
    plt.plot(x, quadratic_regression, color = 'yellow')
    #labeling
    plt.xlabel('Ranking')
    plt.ylabel(data_type)
    plt.title(f"Scatterplot ranking vs {data_type}")
    plt.grid(True)
    plt.legend()
    plt.show()


#r: 0.70-1.00
#Strong accuracy predictor
#r: 0.30-0.69
#Moderate accuracy predictor
#r: 0.00-0.29
#Weak accuracy predictor
#Psychology research: alpha level of 0.05
#Significant effect if <5% probability that the observed difference between groups was due to random chance

#bpm r = -0.037, p = 0.793
#nrgy r = -0.013, p = 0.926
#dnce r = 0.050, p = 0.720
#dB r = -0.056, p = 0.685
#live r = -0.307, p = 0.024
#val r = -0.042, p = 0.763
#dur r = -0.198, p = 0.152
#acous r = -0.097, p = 0.487
#spch r = 0.233, p = 0.090
#pop r = -0.128, p = 0.357

import numpy as np

x = np.linspace(0.0, 5.0)

y = 10.0 + 5.0 * x

data = odr.Data(x, y)

odr_obj = odr.ODR(data, odr.multilinear)

output = odr_obj.run()

print(output.beta)
[10.  5.]