##Goal is to accept a string and total how many times each letter appears in the string.

lstletter = []
sanlstletter = []
counts = {}

name = input("Hello user what is your name? \n")

words = input("Nice to meet you " + name+ ". What words would you like calculated? \n")

upperwords = words.upper()

for sanletter in upperwords:
        if sanletter.isalpha():
                sanlstletter.append(sanletter)


for countedletter in (sanlstletter):
        if countedletter in counts:
                counts[countedletter] += 1
        else:
                counts[countedletter] = 1

for key, value in sorted(counts.items()):
        print (key, ' : ', value)
