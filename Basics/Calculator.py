import math

operand1 = float(input("Enter the first operand : "))
operator = input("The operator used is (+, -, /, *, **) : ")
operand2 = float(input("Enter the second operand : "))

if operator == "+" :
    result = operand1 + operand2
    print(result)
elif operator == "-" :
    result = operand1 - operand2
    print(result)
elif operator == "/" :
    result = operand1 / operand2
    print(result)
elif operator == "*" :
    result = operand1 * operand2
    print(result)
elif operator == "**" :
    result = pow(operand1, operand2)
    print(result)
else :
    print("Syntax Error")