import clear
#from replit import clear

def calc(num1, num2, opr):
  if(opr == "*"):
    return num1 * num2
  elif(opr == "+"):
    return num1 + num2
  elif(opr == "-"):
    return num1 - num2
  elif(opr == "/"):
    return num1 / num2
  else:
    return(0)
    
#main portion of code 

invalid_opr= False    
loop_cal = "y"

while (loop_cal !='n'): 
  num1= int(input("What's the first number?: "))
  print("+\n-\n*\n/") 
  while not(invalid_opr):
    opr = input("Pick an Operation: ") 
    if( opr not in ("*","/","+","-")):
      invalid_opr= False
      print("Enter Valid Operator")
    else:
      invalid_opr= True   
  num2= int(input("What's the next number?: "))
  
  if(opr == "/" and (num1==0 or num2==0)):
    print("Enter Valid number inputs")
  else:     
    result = calc(num1, num2, opr)
    print(f"{num1} {opr} {num2}"" = " f"{result} ")
    loop_cal = input(f"Type 'y' to continue calculating with{result} "," or type 'n' to start a new calculation: ").lower()
    if(loop_cal =="y" ):
      num1 == result
    else:
      clear()
  
