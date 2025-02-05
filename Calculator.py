print("Hello! this is your math assistant")
answer = input("How can I help you today here are what I can do \n 1:addition \n 2:subtraction \n 3:multipltion \n 4:division \n 5:peverity \n")
if answer == "1" :
    x = int(input("What's X: "))
    y = int(input("What's Y: "))
    print(x+y)
elif answer == "2" :
    x = int(input("What's X: "))
    y = int(input("What's Y: "))
    print(x-y)
elif answer == "3" :
    x = int(input("What's X: "))
    y = int(input("What's Y: "))
    print(x*y)
elif answer == "4" :
    x = int(input("What's X: "))
    y = int(input("What's Y: "))
    print(x/y)
elif answer == "5" :
    x = int(input("What's the number: "))
    if x % 2 == 0 :
        print('ODD')
    else:
        print('EVEN')
else:
    print("Please select numbers from 1 -----> 5 only based on what you want assist in ")