i = 0
##2while i == 0: 
hat = input("enter first number\n")

hat = int(hat)

ghst = input("enter operator\n")

hat2 = input("enter second number\n")

hat2 =int(hat2)

def add (hat,hat2):
    results= hat + hat2
    return results
def mult (hat,hat2):
    results = hat * hat2
    return results
def div (hat,hat2):
    results = hat /hat2
    return results
def Min (hat,hat2):
    results = hat - hat2
    return results

if "+" == ghst:
   print (add(hat,hat2))
elif "*" == ghst:
    print(mult(hat, hat2))   
elif "/" == ghst:
    print(div(hat,hat2) )
elif "-" == ghst :
    print (Min(hat, hat2))    
else :
    print ("Invalid operator")    