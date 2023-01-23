#Intermediate Exercise 01
# Write a function that takes in a list data structure as input. The function should create a new 
# list and only include unique elements of the inputted list. Under the function, write code that 
# calls the function with a test list like so and print out the result. 
# Remember that your code should work for all lists of integers, not just the sample test here.

def get_unique_list(tempList):
    newList = tempList
    y = 0
    while y < len(newList):
        if newList.count(newList[y]) > 1:
            newList.remove(newList[y])
        if y == len(newList) - 1:
            break
        y = y + 1
    return newList

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(str(unique_list))