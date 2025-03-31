import random
original = random.randint(100,1000)
print(original)

for i in range(10):
    guess = int(input("make a guess:"))
    if guess==original:
        print("congrats")
        break
    else:
        print("please try again")