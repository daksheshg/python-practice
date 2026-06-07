for i in range(1,21):
    print(i)

fruits=["banana","orange","mango"]
for fruit in fruits:
    print(fruit)

student={
    "name":"Dakshesh",
    "city":"Pune",
    "contact":"7343608858"
}

print(student["contact"])

def greet(name):
    return "Hello "+ name

print(greet("Dakshesh"))

count=len(fruits)
print(count)