#Intermediate Exercise 03
#Take in a string from the user and pass it as input to a function. 
# Have the function return a dict which keeps count of each letter 
# (in lowercase) in the string, excluding spaces. Print out this dict.

def functionReturn(tempString):
    userInput = tempString.lower().replace(' ', '')
    dictList = {}
    for x in range(0, len(userInput)):
        dictList[userInput[x]] = userInput.count(userInput[x])
    return dictList

print('Enter a string: ', end= '')
userWord = input()
print(functionReturn(userWord))