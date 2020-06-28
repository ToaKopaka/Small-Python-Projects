numList = []        #Set a variable for the list
GoodInput = True #Set a sentinal for good input 
try:
    for num in range(1,11): #Set loop for user to enter 10 numbers as ints
        number = int(input("Give me a number: "))
        numList.append(number)
except ValueError: #Check for good input
    print("You did not enter a number")
    GoodInput = False

numList.sort() #Sort the list to get lowest and highest numbers

total = 0
for value in numList: #Set loop for add in the total of all the numbers in the list
    total += value

if GoodInput == True: #If the input is good set these variables
    Low = numList[0]
    High = numList[-1]
    LowHigh = Low + High

    
if GoodInput == True: #If input is good print outcome
    print("The lowest number in the list is" , numList[0])
    print("The highest number in the list is" , numList[-1])
    print("The average of the highest and lowest numbers is" , LowHigh / 2)
    print("The total is", total)



