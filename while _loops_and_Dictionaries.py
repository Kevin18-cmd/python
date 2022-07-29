friends = input("how many friends do you have ?\n")
friends = int(friends)
i = 1
while i <= friends:
    put= input ("enter friends name\n ")
    yuk = int(input ("enter their birth month\n"))
    months = {
        1:"january",
        2:"february",
        3:"march",
        4:"april",
        5: "may",
        6:"june",
        7:"july",
        8:"august",
        9:"september",
        10:"october",
        11:"november",
        12:"December"
    }
    print (put + " was born in "+ months.get(yuk))
    i +=1
