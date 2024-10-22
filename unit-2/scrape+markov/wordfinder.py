from os import listdir, path
file = open("output.txt")
word_count = {}
frequent_words = ["the", "a", "and", "of", "to", "on", "is", "are", "there", "this", "that", "1", "2", "3", "4"] # I was geting "2" as the most frequent word so I put 1-4 in this list just in case.
for line in file:
    for word in line.split():
        # .split() split a string into a list where each word ia a list item
        if word in frequent_words:
            continue
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
allPairs = iter((word_count.items()))
firstPair = next(allPairs)

mostfrequent = firstPair[0]
for word in word_count:
    if word_count[word] > word_count[mostfrequent]:
        mostfrequent = word
print("\n the most frequent word is:", mostfrequent, "\n it appears", word_count[mostfrequent], "times" )
