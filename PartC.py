import re
from itertools import groupby, chain

input1 = []
with open("Input1.txt", "r") as f1:
    for line in f1:         #parse file line by line
        ls = re.split(", |\n", line)        #split the words by ", " and "\n"
        temp = (ls[0], int(ls[1]))
        input1.append(temp)             #List of tuples
#print input1

input2 = []
with open("Input2.txt", "r") as f2:
    for line in f2:
        ls = re.split(", |\n", line)
        temp = (ls[0], int(ls[1]))
        input2.append(temp)
#print input2

input = sorted(chain(input1, input2), key=lambda x: x[0])       #combine and sort

output = {}
for key, group in groupby(input, key=lambda x: x[0]):           #group is based on key. O(m+n)
    output[key] = sum(x[1] for x in group)          #reducing to one map

with open("PartC_Output.txt", "w") as f3:
    for w in sorted(output):
        f3.write(w + ", " + str(output[w]) + "\n")

