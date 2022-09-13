import random

secret = random.randint(1,10)
guess = random.randint(1,10)

print("Guess value is = ", guess)
print("Secret value is = ", secret)

if guess < secret:
    print("too low!")

elif guess > secret:
    print("too high!")

else:
    print("just right!")