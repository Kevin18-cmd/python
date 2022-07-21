start=input ()
start= int(start) 
if start == start:
 char =int( input ("enter first number\n "))
print ("press 1 for multiplication, 2 for additiion, 3 for subtraction and 4 for division")
cat1 = input()
char1 = int( input ("enter second number\n "))
#5print ("press 1 for multiplication, 2 for additiion, 3 for subtraction and 4 for division")
#cat1 = input()
cat=int(cat1)
if cat == 1:
    print ("the answer is " + str(char*char1))
elif cat== 2:
    char2 = char + char1
    print ("the answer is " + str(char2))
elif cat == 3:
    char3 = char-char1
    print("the answer is " +str(char3))    
elif cat == 4:
    print("the answer is " + str(char/char1)) 
else :
   print ("select operation")  