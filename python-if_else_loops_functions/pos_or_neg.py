import random
number = random.randint(-1000, 1000)
if number < 0:
	print(f"{number} is negative")
elif number == 0:
	print(f"{number} is zero")
else:
	print(f"{number} is positive")
