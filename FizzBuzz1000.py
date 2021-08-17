import random

def FizzBuzz(r):
    if r % 3 == 0 and r % 5 == 0:
        print("FizzBuzz")
    elif r % 3 == 0:
        print("Fizz")
    elif r % 5 == 0:
        print("Buzz")
    print("\n")

for i in range(0, 1000):
    r=random.randint(0,100)
    print("Round: %d"%i)
    print("Random: %d"%r)
    FizzBuzz(r)
