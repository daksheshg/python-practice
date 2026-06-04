student = {
    "name": "John",
    "age": 22
}

print(student["name"])

student["city"] = "Pune"

print(student["city"])

student["age"] = 25

for key,value in student.items():
    print(key,"-",value)

