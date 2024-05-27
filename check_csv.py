import csv
f = open("organizeyourmusic_formatted.csv", 'r')
csvReader = csv.reader(f)
length = 0
temp = True
for i, row in enumerate(csvReader):
    if i==0:
        length = len(row)
    print(row)
    if len(row) != length:
        temp = False
print(temp)

