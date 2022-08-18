class cal():
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def barathAdd(self):
        return self.x + self.y

    def barathSub(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    # This function divides two numbers
    def divide(self):
        return self.x / self.y


while True:

    choice = input("Enter Choice 1/2/3/4 = ")

    if choice in ('1','2', '3', '4'):
        print("condition 1")
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))

        obj=cal(x,y)

        if choice == '1':
            print("condition 2")
            print(obj.barathAdd())

        elif choice == '2':
            print("condition 3")
            print(obj.barathSub())

        elif choice == '3':
            print("condition 3")
            print(obj.multiply())

        elif choice == '4':
            print("condition 3")
            print(obj.divide())

        next_calculation = input("Another Calculation (yes/no)")
        if next_calculation == 'no':
            break

    else:
        print("condition 4")
        print("invalid input")

    
