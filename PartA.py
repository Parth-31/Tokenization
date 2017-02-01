import re     #import Regex


class Tokenizer():

    def tokenize(self, f):
        tokens = []
        for line in f:    #line by line add every token to list
            tokens.extend([i.lower() for i in re.split(r'(\W+)', line) if i.isalnum()])
        return tokens

    def computeWordFrequencies(self,ls):
        cmap = {}
        for word in ls:      #for evry word in list, make hashmap(dictionary)
            if cmap.has_key(word):
                cmap[word] = cmap.get(word) + 1
            else:
                cmap[word] = 1
        return cmap

    def print_sorted(self, frequency):
        for w in sorted(frequency, key=frequency.get, reverse=True):   #sort dictionary in reversed order based on the value
            print w, frequency[w]


f1 = open("a1.txt", "r")    #open the file

tok = Tokenizer()       #instance of the class
ls_token = tok.tokenize(f1)
mp_freq = tok.computeWordFrequencies(ls_token)
tok.print_sorted(mp_freq)






