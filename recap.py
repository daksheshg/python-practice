fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

numbers = [12, 5, 8, 99, 34]
largest = numbers[0]
for number in numbers:
    if number>largest:
        largest = number
    
print("Largest number is",largest)

student = {
    "name": "Dakshesh",
    "city": "Pune"
}

print(student["name"])

for name,city in student.items():
    print(f"{name} - {city}")

def average(numbers):
    length=len(numbers)
    total=sum(numbers)
    average=total/length
    return average

print(average([10,20,30]))

fruits = ["apple", "banana", "orange"]
for position,fruit in enumerate(fruits,start=1):
    print(f"{position}. {fruit}")

text = "apple banana apple orange apple"
words=text.split()
counts={}
for word in words:
    if word in counts:
        counts[word]+=1
    else:
        counts[word]=1
print(counts)

contacts = {
    "John": "111",
    "Sarah": "222"
}

def find_contact(name):
    if name in contacts:
        print(f"{name} - {contacts[name]}")
    else:
        print("Contact not found")

find_contact("Sarah")
find_contact("Emma")

name = "Dakshesh"
age = 25

print(f"Name = {name}")
print(f"Age = {age}")

students = {
    "John": 85,
    "Sarah": 92,
    "Mike": 78
}

print("Student list")
for position,(name,grade) in enumerate(students.items(),start=1):
    print(f"{position}. {name} - {grade}")

grades=students.values()
print(grades)

total=sum(grades)
number=len(grades)
avg=total/number
highest=max(grades)
print(f"Average grade: {avg}")
print(f"Highest grade: {highest}")