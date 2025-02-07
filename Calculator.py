#creating the addition function
def addition():
    A = int(input("enter the first number: "))
    B = int(input("enter the seconde number: "))
    C = A + B
    print("The result is ", C , "\n")

#creating the substraction function
def substraction():
    A = int(input("Enter the first number: "))
    B = int(input("Enter the second number: "))
    C = A - B
    print("The result is ", C , "\n")

#creating the multiplication function
def multuplication():
    A = int(input("Enter the first number: "))
    B = int(input("Enter the seconde number: "))
    C = A * B
    print("the result is ", C, "\n")

#creating the division function
def division():
    A = int(input("Enter the first number: "))
    B = int(input("Enter the seconde number: "))
    C = A / B
    print("The result is ", C, "\n")

#creating the function that define if a number is odd or even
def oddeven():
    A = int(input("Enter a number: "))
    R = A % 2
    if R == 0:
        print("EVEN \n")
    else:
        print("ODD \n")

#greeting the user and introduction the calculator for him
print("Hello! this is your math assistant")
print("How can I help you today here are what I can do")

#creating a loop and the conditionals
while True :
    options = input(" 1:addition \n 2:subtraction \n 3:multuplication \n 4:division \n 5:Check if number is odd or even \n 6:Stop\n")
    if options == "1" :
        addition()
    elif options == "2" :
        substraction()
    elif options == "3" :
        multuplication()
    elif options == "4" :
        division()
    elif options == "5" :
        oddeven()
    elif options == "6" :
        print("Goodbye!")
        exit()
    else:
        print("Please select a number from 1 to 6 base on what you want from the menu \n")
#end