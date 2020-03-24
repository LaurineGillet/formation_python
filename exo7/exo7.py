from random import randint
a = randint(0, 200)
with open("file.txt", "w") as file:
        print (a)
        file.write(str(a))

