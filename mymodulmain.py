# Kalle mymodultest
import mymodultest
import math
from mymodultest import greet, classify_age

message = mymodultest.greet("Dennis")
print(message)

# age classification
try:
    user_age = int(input("Enter your age: "))
    result = classify_age(user_age)
    print(result)
except ValueError:
    print("Error: Invalid input. Please enter a number")

# math
print (f"Squareroot of 16 is {math.sqrt(16)}")
print (f"Squareroot of 25 is {math.sqrt(25)}")
# Sine, cosine, tangent
print (f"Sine (sinus) of 45 degrees is {math.sin(math.radians(45))}")
# power
print (f"2 raised to the power of 3 is {math.pow(2,3)}")