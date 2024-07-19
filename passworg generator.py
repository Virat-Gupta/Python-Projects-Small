import random

charList = [['a','b','c','d'],['A','B','C','D'],[1,2,3,4],['@', '#', '$', '%']]
length = int(input("ENTER LEN:"))

password = ""

for _ in range(0,length) :
    password += str(random.choice(random.choice(charList)))

print(password)
