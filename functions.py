def greet(name):
    return f"Hello {name}"

print(greet("Dakshesh"))

def square(number):
    return number**2

print(square(4))

def is_even(number):
    if number%2==0:
        return "Even"
    else:
        return "Odd"
    
print(is_even(6))

def calculate_total(numbers):
    sum=0
    for i in numbers:
        sum+=i
    return sum

print(calculate_total([1,2,3,4,5]))