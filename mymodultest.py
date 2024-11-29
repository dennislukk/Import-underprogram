#Function
def greet (name):
    return f"Hello, {name}"

def classify_age (age):
    if age < 0:
        return "Error: Age cannot be negative"
    if age < 18:
        return "You are a minor"
    return "You are an adult"

