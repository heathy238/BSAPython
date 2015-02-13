firstNumber = int(input("Enter a number between 1 and 100: "))
secondNumber = int(input("Enter another number between 1 and 100: "))
bot = input("Enter a maths sybles to calculate things")

if bot == "+":
    print(firstNumber, "+", secondNumber, "=",firstNumber+secondNumber)
elif bot == "-":
    print(firstNumber, "-", secondNumber, "=",firstNumber-secondNumber)
elif bot == "/":
    print(firstNumber, "/", secondNumber, "=",firstNumber/secondNumber)
elif bot == "*":
    print(firstNumber, "*", secondNumber, "=",firstNumber*secondNumber)
else:
    print ("sorry that not valid")
number = 2
time.sleep(2)
while number>0:
    number = number*number
    print(number)
