i = 0
##while i == 0: 
hat = input("enter first number\n")

hat = int(hat)

ghst = input("enter operator\n")

hat2 = input("enter second number\n")

hat2 =int(hat2)

if "+" == ghst:
   result = hat + hat2
   print (result)
elif "*" == ghst:
    result = hat * hat2
    print(result)   
elif "/" == ghst:
    result = hat / hat2
    print(result)
elif "-" == ghst :
    result = hat - hat2
    print (result)    
else :
    print ("Invalid operator")    