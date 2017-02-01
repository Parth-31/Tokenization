import re

class Intersection():

    def tokenize(self, f):
        tokens = []
        for line in f:
            tokens.extend([i.lower() for i in re.split(r'(\W+)', line) if i.isalnum()])
        return tokens

    def intersection(self,ls1,ls2):
        #return [val for val in set(ls1) if val in set(ls2)]
        return set(ls1).intersection(set(ls2))         #O(min(len(ls1), len(ls2)), worst O(len(ls1) * len(ls2)) //Stackoverflow


tok = Intersection()        #instance of class

f1 = open("a1.txt","r")
ls1 = tok.tokenize(f1)      #List of tokens of first file

f2 = open("a2.txt","r")
ls2 = tok.tokenize(f2)      #List of token of second file

common = tok.intersection(ls1,ls2)
#print common
print len(common)






