import csv
f = open("3_top100_formatted.csv", 'r')
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

