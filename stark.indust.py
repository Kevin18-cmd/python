print ("welcome to te stark industries student platform")
login = input("enter your student number to login\n")
login =int(login)
student_numbers = [2018238485,201825768]
if login == student_numbers[0]:
    print ("welcome Kevin\n"
    "program:Information and Communication Tech\n"
    "currrent year of study: fourth")
elif login == student_numbers[1]:
    print("welcome john\n")    
else :
    print ("User not found kindly register, thank you")    