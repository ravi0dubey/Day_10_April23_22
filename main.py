from art import logo
import clear

def add(num1,num2):
  return num1 + num2
def subtract(num1,num2):
  return num1 - num2
def multiply(num1,num2):
  return num1 * num2 
def divide(num1,num2):
  return num1 / num2

#Dictionary for Operations
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
  }    

#main portion of code 

def calculator():
  print(logo)
  loop_cal = " "
  
  while (loop_cal !='n'): 
    if(loop_cal !="y" ):
      num1= int(input("What's the first number?: "))
    for oper in operations:
     print(oper)
    invalid_opr= False   
    while not(invalid_opr):
      oper = input("Pick an Operation: ") 
      if(oper not in ("*","/","+","-")):
        invalid_opr= False
        print("Enter Valid Operator from above list")
      else:
        invalid_opr= True   
    
    cal_function = operations[oper]
    num2= int(input("What's the next number?: "))
    result = cal_function(num1,num2)
  
    print(f"{num1} {oper} {num2}"" = " f"{result} ")
  
    print(f"Type 'y' to continue calculating with {result}"," or type 'n' to start a new calculation: \n")
    loop_cal = input()
    
    if(loop_cal =="y" ):
       num1 = result
    else:
      calculator()
  
#call Calculator function
calculator()
