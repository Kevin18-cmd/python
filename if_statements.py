num1 = input ("enter first number\n" )

num2 = input ("enter second number\n")

num3 = input ("enter last number\n")

def max(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2    
    elif num3>=num1 and num3>=num2:
        return num3
print("the greatest number is "+ (max(num1,num2,num3)))    