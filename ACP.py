
try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma: "))
    operation = int(input(("Choose an operation: \n 1) Addition \n 2) Subtraction \n 3) Multiplication \n 4) Division \n Enter your answer: ")))

    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        return a/b

    if operation == 1:
        print(f"{num1} plus {num2} is: ", add(num1,num2))
    elif operation == 2:
        print(f"{num1} minus {num2} is: ", sub(num1,num2))
    elif operation == 3:
        print(f"{num1} times {num2} is: ", mul(num1,num2))
    else:
        print(f"{num1} divided by {num2} is: ", div(num1,num2))
except ZeroDivisionError:
    print("You cant divide by zero!")
except ValueError:
    print("Use digits only.")
except SyntaxError:
    print("Use a comma between the 2 numbers.")
except:
    print("Enter two numbers")