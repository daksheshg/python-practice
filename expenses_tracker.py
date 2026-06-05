expenses=[]
def add_expenses(expense):
    expenses.append(expense)

def show_expenses():
    for position, expense in enumerate(expenses, start=1):
        print(f"Expense {position} - {expense}")
        

def total_expenses():
    print("Total Expenses=",sum(expenses))

add_expenses(500)
add_expenses(1000)
add_expenses(1500)
show_expenses()
total_expenses()