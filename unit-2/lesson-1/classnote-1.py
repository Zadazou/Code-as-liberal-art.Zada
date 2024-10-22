## ## ###
## class work from 10/9
## ## ###
# myList = ["rae", "is", "coding"]

# # # print(myList)

# myList.append("today")

# # print(myList)

# isRaeInList = "rae" in myList

# print(isRaeInList)

# university = {}
# university["subject"] = "theory"
# university["course"] = "coding as a liberal art"
# university["department"] = "eugene lang"
# university["students"] = ["beimnet", "badah", "kirsten", "miranda"]

# print(university)

## ## ###
## more list review
## ## ###
# myList = []
# myList.append("rae")

# myList.append("bruml")
# isPersonOnList = "bruml" in myList
# print(isPersonOnList)

# ## ## ###
# ## more dictionary review
# ## ## ###
university = {}
university["subject"] = "theory"
university["department"] = "liberal arts"
university["course"] = "coding"

checkForDept = "department" in university
print(checkForDept)
print("Department is in this dictionary:", checkForDept)

students = ["zada", "chris", "sigrid"]
university["roster"] = students
# print(university)

# print("----\n----\n-----")
# ## # see the key and value pairs
# for x in university:
#     print( x, "----->", university[x])

# print("----\n----\n-----")


## ## ###
## more dictionary for loop review
## ## ###

# to see each tuple one at a time so you can iterate through them, .items() gives you each item as a tuple, .values() gives you each value so that you can check what type of data it is 

university["total"] = 0

for item in university.items():
    # print(item)
    for x in item:
        if (type(x) is list):
            print("This is not a string, but there are", len(x), "items in this list!!")
            
            for i in x:
                university["total"] = university["total"] + 1
                
        if (type(x) is str):
            print("there are", len(x), "characters in this string:", x)


print("----\n----\n-----")

print("Total number of students:", university.get("total"), "Their names are:", students)
# for stu in university["roster"]: 
#     print(stu)

# print("----\n----\n-----")