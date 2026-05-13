#calculator

def calculate (  a , operator , b):
    if operator == "+":
        result = a + b 
    elif operator == "-":
        result = a - b 
    elif operator == "*":
        result = a * b
    elif operator == "/":
        try :
            result = a / b
        except ZeroDivisionError :
            result = 0
            print("zero division error !")
            
    return result 

user = input("Enter Exit / Start :")
try:
    while True :
        if user == "exit":
            break
        operator = input("+ , - , / , * :") 
        if operator not in ["+" , "-" , "*","/"]:
            print("not matched !")
        else:
            a = int(input("Enter number : "))
            b = int(input("Enter second number : "))
            calculator = calculate(a ,operator , b)
            print(calculator)
except ValueError as e :
    print("Enter only numbers !")
    

      


