import argparse
import numpy as np
import string

def main():
    userInput = input("Entrez le mot a crypter: ")
    
    alphabet = [(0,'A'), (1 , 'B'), (2 , 'C'), (3 , 'D'), (4 , 'E'), (5 , 'F'), (6 , 'G'), (7 , 'H'), (8 , 'I'), (9 , 'J'), (10 , 'K'), (11 , 'L'), (12 , 'M'), (13 , 'N'), (14 , 'O'), (15 , 'P'), (16 , 'Q'), (17 , 'R'), (18 , 'S'), (19 , 'T'), (20 , 'U'), (21 , 'V'), (22 , 'W'), (23 , 'X'), (24 , 'Y'), (25 , 'Z')]
    wordToCrypt = []
    numberLetter = []
    for e in list(userInput):
        numberLetter.append(str(string.ascii_lowercase.index(e)))
    key = np.matrix('15 0 15 12; 22 8 14 2; 14 6 23 1; 8 1 6 5') #With keys POP WIT OGH
    print(key," \n--------\n")
    s = ';'
    s = s.join(numberLetter)
    print(s)
    userMessage = np.matrix(s)
    print(userMessage," \n--------\n")
    rlt = np.matmul(key, userMessage)
    print(rlt," \n--------\n")
    result = userMessage
    index = 0
    cryptedWord =""
    for i in rlt:
        for e in i:
            value = int(e%26)
            result[index,0] = value
            cryptedWord+=dict(alphabet)[value]
            index+=1

    print(result) #TGC

    print(cryptedWord)

if __name__ == "__main__":
    main()