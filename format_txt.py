import os

file = open("organizeyourmusic_raw.txt", "r")
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
with open('output.txt', 'w') as f:
    f.writelines(lines)