from main import maincalculator
while True:
 num1 = int(input("Enter the first number: "))
 oper = "Adding(+),\n Substracting(-),\n Divide(/),\n Multiply(*), \n Square(**), \n Square root(1/2), "
 operator = input(f"Choose one opperation {oper} \n: ")
 """if operator == "**":
     maincalculator(num1,operator)
 elif operator == "1/2":
     maincalculator(num1,operator)
 else:"""

 maincalculator(num1,operator)