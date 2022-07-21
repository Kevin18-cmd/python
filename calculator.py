
char =int( input ("enter first number\n "))
print ("enter operator: ")
cat = input()
char1 = int( input ("enter second number\n "))
if cat == "*":
    print ("the answer is " + str(char*char1))
elif cat== "+":
    char2 = char + char1
    print ("the answer is " + str(char2))
elif cat == "-":
    char3 = char-char1
    print("the answer is " +str(char3))    
elif cat == "/":
    print("the answer is " + str(char/char1)) 
else :
   print ("select operation")  