secret_word =["computer","phone","Television","laptop"]
guess_word =""
guess_limit = 3
guess_count = 0
Out_of_guesses = False
while guess_word != secret_word and not(Out_of_guesses):
    
    if guess_count <  guess_limit:
     print("hint \n Its an elictronic used on a daily basis")   
     guess_word = input("Enter your guess\n")
     if guess_word != secret_word:
        print("no...try agian")
     guess_count += 1
    else :
     Out_of_guesses = True 

if Out_of_guesses:
 print("out of guesses,you lose")        
else:
 if guess_count <= 2:
    number_limit = 0
    number = 0
    while  number_limit != 4:
       random_number = input("enter any number between 1 and 10 ")
       random_number1 = int(random_number)
       if random_number1 <= 0 or random_number1 > 10:
        print("please enter number between 1 and 10 \n")   
       else:
        number += random_number1
        number_limit += 1           
    if number == 0:
            print ("aww..sorry you cant continue, but hey you go the first one right")   
    else :
          total = str(number)
          print("well thank you for playing, you win and sum off your numbers is " + total)     
  
  
