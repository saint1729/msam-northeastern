name = input("Hello! What is your name? ")
print(f"Nice to meet you, {name}")
age = int(input("How old are you? "))
MY_AGE = 20
if age == MY_AGE:
    print("Omg! We are the same age!")
elif age > MY_AGE:
    print(f"Oh, I am {age - MY_AGE} years younger than you are!")
else:
    print(f"Oh, I am {MY_AGE - age} years older than you are!")
