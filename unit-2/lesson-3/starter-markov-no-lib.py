import pprint

file = open("4-text-small.txt").read().lower()

markovDictionary = {}

words = file.replace("\n"," ").split()

for (i, word) in enumerate(words):
    
    if i == len(words) - 1:
        break

    next_word = words[i+1]
    
    if word in markovDictionary:
        markovDictionary[word].append(next_word)
    else:
        markovDictionary[word] = [next_word]

# # print(markovDictionary)
# # use pretty print library to see dictionary more clearly
pprint.pp(markovDictionary)

