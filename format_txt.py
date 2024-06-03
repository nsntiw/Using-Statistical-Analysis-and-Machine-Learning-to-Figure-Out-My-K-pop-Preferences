import os

file = open("1_top100_raw.txt", encoding = "utf-8")
lines = file.readlines()

lines = [line.replace('\t', ",") for line in lines]
lines = [line[line.find(",,,")+3:] for line in lines]
for line in lines:
    for word in line.split(","):
        if word.count("â€‘") ==2:
            word.replace("â€‘", "/")
            print(word)
        #print(word)
#lines = [line.replace('‑', "/") for line in lines]

# finally, write lines in the file
with open('output.txt', 'w', encoding="utf-8") as f:
    f.writelines(lines)