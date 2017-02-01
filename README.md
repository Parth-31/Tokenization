# Tokenization
This is file tokenization project in python. This can be further used in web crawling.

*-> Part A: Word Frequencies

Write a method/function that reads in a text file and returns a list of the tokens in that file. For the purposes of this project, a token is a sequence of alphanumeric characters, independent of capitalization (so Apple, apple are the same token).
Method/Function: List<Token> tokenize(TextFilePath)

Write another method/function that counts the number of occurrences of each word in the token list.
Method: Map<Token,Count> computeWordFrequencies(List<Token>)

Finally, write method that prints out the word frequency counts onto the screen. The print out should be ordered by decreasing frequency. (so, highest frequency words first)
Method: void print(Frequencies<Token,Count>)

*-> Part B: Intersection of two files
Write a program that takes two text files as arguments and outputs the number of tokens they have in common.

*-> Part C: Reducing two Word-Frequency Counts
Write a program that takes two word-frequency maps (given in two separate input text files) and creates an output word-frequency count file where the counts are added. The input and output files are of the form “word, count”, one of these per line. 
