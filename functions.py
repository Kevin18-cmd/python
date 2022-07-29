
name = input ("what is your name :\n")
age1 = input ("how old are you:\n")
name2 = input ("whats your name:\n")
age2 =input("how old are you:\n")
names =[] 
names.insert(0,name)
names.insert(1,name2)
age =[]
age.append(age1)
age.append(age2)
def greet(name,age):
    print("hello "+name+" youre "+str(age)+" years old")
greet(names[0],age[0])
greet(names[1],age[1])
print("thanks for participating")


