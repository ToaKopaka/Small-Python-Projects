import random
EvenOrOdd = random.randint(1,2)   #See if it will be an addition or subtraction
Num1 = random.randint(1,50)
Num2 = random.randint(1,50) #Get the random numbers
if EvenOrOdd == 1:
    print("Please enter the answer to",Num1,"+",Num2) #If it's an addition it will run this block
    Answer = int(input(": "))
    if Answer == (Num1 + Num2):
        print("Correct!")
    else:
        print("That is not correct. The answer is", Num1 + Num2)
elif EvenOrOdd == 2:
    print("Please enter", Num1, "-", Num2)
    Answer = int(input(": "))                   #If it's a subtraction it will run this block
    if Answer == (Num1 - Num2):
        print("Correct!")
    else:
        print("That is not correct. The answer is", Num1 - Num2)
