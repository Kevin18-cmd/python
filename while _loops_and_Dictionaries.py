friends = input("how many friends do you have ?\n")
friends = int(friends)
i = 1
while i <= friends:
    put= input ("enter friends name\n ")
    yuk = int(input ("enter their birth month\n"))
    months = {
        1:"january",
        2:"february",
    }
    print (put + " was born in "+ months.get(yuk))
    i +=1
