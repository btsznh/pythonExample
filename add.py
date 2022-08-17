def barathAdd(x,y):
    return x + y

def barathSub(x,y):
    return x - y



while True:

    choice = input("Enter Choice 1/2 = ")

    if choice in ('1','2'):
        print("condition 1")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        if choice == '1':
            print("condition 2")
            print(barathAdd(x,y))

        elif choice == '2':
            print("condition 3")
            print(barathSub(x,y))

        next_calculation = input("Another Calculation (yes/no)")
        if next_calculation == 'no':
            break

    else:
        print("condition 4")
        print("invalid input")

    
