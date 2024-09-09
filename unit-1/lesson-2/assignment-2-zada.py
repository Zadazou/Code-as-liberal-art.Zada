from unit1lesson2 import * # * means every thing

1.
#number_list.sort()
#print(number_list[0])
1.
# smallest_number = number_list[0]
# for n in number_list:
#     if n < smallest_number:
#         smallest_number = n
# print(smallest_number)

# answer is 175

2.
# number = [num for num in number_list if num > 500]
# number.sort()
# print(number[0])
2.
# number = [num for num in number_list if num > 500]
# number_smallerthan500 = number[0]
# if number[1] < number[0]:
#     number_smallerthan500 = number[1]
# for n in number:
#     if n < number_smallerthan500:
#         number_smallerthan500 = n
# print(number_smallerthan500)

# answer is 501

3. 
# number = [num for num in number_list if num % 2 == 0]
# number.sort()
# print(number[0])
3.
# def sortSmallToBig(number_list):
#     smallest_number = number_list[0]
#     for n in number_list:
#         if n < smallest_number:
#             smallest_number = n
#     return smallest_number
# even_numbers = []
# for num in number_list:
#     if num % 2 == 0:
#         even_numbers.append(num)
# smallestEven = sortSmallToBig(even_numbers)
# print(smallestEven)
   
#answer is 176

4.
# word = word_list[0]
# if word_list[1] > word_list[0]:
#     word = word_list[1]
# for w in word_list:
#     if w > word:
#         word = w
# print("the last alphabetically word is", word)
    
#answer is violation

5.
# longestword = word_list[0]
# if len(word_list[1]) > len(word_list[0]):
#     longestword = word_list[1]
# for w in word_list:
#     if len(w) > len(longestword):
#         longestword = w
# print(longestword)

# the word is rehabilitation