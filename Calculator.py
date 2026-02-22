def calculator(num1, num2, op):
     if (op == "+"):
        print(f" The Sum is {num1+num2}")
     elif (op == "-"):
        print(f" The Difference is {num1-num2}")   
     elif (op == "*"):
        print(f" The Product is {num1*num2}")  
     elif (op == "/"):
        print(f" The Divison is {num1/num2}")  
     elif (op == "%"):
        print(f" The Modulo is {num1%num2}")  
     elif (op == "**"):
        print(f" The Exponential is {num1**num2}")  
     else :
        print("Wrong Input")

num1 = int(input("Enter the First Operand :"))
num2 = int(input("Enter the Second Operand :"))
op = input("Operator (+, -, *, /, %, **) :")

result = calculator(num1,num2,op)
print(result)