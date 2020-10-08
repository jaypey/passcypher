import argparse
import numpy as np
import string

def main():
    userInput = input("Entrez le mot a crypter: ")
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
            cryptedWord+=list(string.ascii_lowercase)[value]
            index+=1

    print(result) #TGC

    print(cryptedWord)

if __name__ == "__main__":
    main()