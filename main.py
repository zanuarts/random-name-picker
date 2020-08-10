import random

name = [
    "Zoeji", "Zanuar"
]

print ("All name : " , name)

pick = random.randint(0, len(name)-1)

print("Picked name : " , {name[pick]})