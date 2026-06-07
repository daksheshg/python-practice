numbers=[12,4,6,8,17,10,65,1]
largest=numbers[0]
for num in numbers:
        if largest<num:
                largest=num
print(largest)

words = ["apple", "apple", "banana", "orange", "banana", "apple"]
count={}
for word in words:
        if word in count:
                count[word]+=1
        else:
                count[word]=1
print(count)

def average(numbers):
        total=sum(numbers)
        count=len(numbers)
        avg=total/count
        return avg
print(average([10,20,30,40,50,60]))

student = {
    "name":"Dakshesh",
    "city":"Pune"
}

for key,value in student.items():
        print(key,":",value)

fruits=["apple","banana","orange","mango","papaya","watemelon"]
select=int(input("Enter 1 for Viewing fruits\n 2 for Add Fruits\n 3 for Exit:"))
if select==1:
        for fruit in fruits:
                print(fruit)
elif select==2:
        add_fruit=(input("What fruit you want to add:"))
        fruits.append(add_fruit)
        print(fruits)
else:
        print("Thank you")


