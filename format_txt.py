import os

file = open("organizeyourmusic.txt", "r")
lines = file.readlines()

lines = [line.replace('\t', ",") for line in lines]
lines = [line[line.find(",,,")+3:] for line in lines]
# finally, write lines in the file
with open('output.txt', 'w') as f:
    f.writelines(lines)