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


while True :
    user = input("Enter Exit / Start :")
    User = user.lower()
    if User == "exit":
            print("--Calculator is closed--")
            break
    elif User == "start":
        while True:
            operator = input("+ , - , / , * :") 
            if operator not in ["+" , "-" , "*","/"]:
                print("not matched !")
            else:
                try:
                    a = int(input("Enter number : "))
                    b = int(input("Enter second number : "))
                    calculator = calculate(a ,operator , b)
                    print("--calculation--")
                    print(calculator)
                    break
                except ValueError as v :
                    print("put only integer values !")
                    
     
                
                
    

      


