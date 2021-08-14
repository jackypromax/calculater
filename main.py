def maincalculator(num1,operator,num2=0):

 if operator == "**" and "square":
    squa = num1**2
    print(squa)

 elif operator == "1/2" and "Square root":
    sqr = num1*1/2
    print(sqr)

 else:
    num2 = int(input("Enter the second number: "))


 if operator == "+" and "add":
     ad = num1+num2
     print(ad)
 if operator == "-" and "Sub":
    su = num2-num1
    print(su)
 if operator == "/" and "divide":
    did = num2/num1
    print(did)
 if operator == "*" and "Multiply":
    mul = num1*num2
    print(mul)


