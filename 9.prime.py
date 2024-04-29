# if a number is prime or not
number = int(input("enter a number: "))

for i in range(2, number):
    if (number % i == 0):
        print("not a prime")
        break
else:
    print("a prime")