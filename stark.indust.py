print ("welcome to te stark industries student platform")
student_numbers = [2018238485,201825768]
student_names = []
i = 0
while i <= 1 :
 Input = input("press 1 to login and 2 to register\n")
 Input = int(Input)

 if Input == 1: 
  login = input("enter your student number to login\n")
  login =int(login)
  if login == student_numbers[0]:
    print ("welcome Kevin\n"
    "program:Information and Communication Tech\n"
    "currrent year of study: fourth")
  elif login == student_numbers[1]:
    print("welcome john\n"
     "program:Information and Communication Tech\n"
     "currrent year of study: fourth")    
  elif login == student_numbers[2]:
     print("Welcome " + student_names[0])
     print ("program " +Student_program )
     print ("you are currently in you "+ str(student_year )+ " year") 
  else :
    print ("User not found kindly register, thank you")    
 elif Input == 2:
  Student_number = input ("enter student number\n")
  Student_number  = int(Student_number) 
  student_numbers.append(Student_number)  
  Student_name = input("Enter your name\n ")
  student_names.append(Student_name)
  Student_program =input("What program are you studying\n")
  student_year = input ("what year are you currently in\n ")
  student_year = int(student_year)
 i  += 1 
