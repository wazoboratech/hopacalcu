history = []
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b == 0:
        return "Error"
    else:
        return a/b
    
while True:
    try:
        num1 =float(input("enter first number:"))
        operation = input("enter operation + - * /:")

        if operation == "h":
            print("last 5 calc:")
            for item in history:
                print(item)
            continue  
        num2 = float(input("enter the second number:"))

        if operation == "+":
           result = add(num1, num2)
        elif operation == "-":
            result = subtract(num1, num2)
        elif operation == "*":
            result = multiply(num1,num2)
        elif operation == "/":
            result = divide(num1, num2)
        else:
            result = "Error, invalid input, use + - * /"
        if isinstance(result, float):
            result= round(result, 2)
        print("result:", result)

        if isinstance(result, float):
            history.append(f"{num1} {operation} {num2} = {result}")
            if len(history) > 5:
                history.pop(0)
                           
    except  ValueError:
        print("Error: Type numbers only")
        continue

    again = input("calculate again? y/n:  ")
    if again == "n":
        print("Bye! hopecalc shutting down.")
        break
        