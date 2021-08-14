def maincalculator(num1,operator,num2=0):
 
# findig square 

 if operator == "**" and "square":
    squa = num1**2
    print(squa)
    
#finding square root
 elif operator == "1/2" and "Square root":
    sqr = num1*1/2
    print(sqr)

 else:
    num2 = int(input("Enter the second number: "))

#adding two numbers
 if operator == "+" and "add":
     ad = num1+num2
     print(ad)
  #subtracting two number
 if operator == "-" and "Sub":
    su = num2-num1
    print(su)
  #dividing two number
 if operator == "/" and "divide":
    did = num2/num1
    print(did)
   
  #multiply two number
 if operator == "*" and "Multiply":
    mul = num1*num2
    print(mul)


