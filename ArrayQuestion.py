monthly_expenses = [2200,2350,2360,2130,2190]
extra = monthly_expenses[1] - monthly_expenses[0]
print(extra)
# 1 In Feb, how many dollars you spent extra compare to January?
extraExpInFeb = print(f"I spent {extra} dollars in feb than jan")


# 2 Find out your total expense in first quarter (first three months) of the year.
def expensesInQuarter(monthly_expenses):
    total = 0  # Initialize total to 0
    for i in monthly_expenses[0:3]:  # Iterate through the first three elements of monthly_expenses
        total += i  # Add each monthly expense to total
    return total  # Return the total
# Call the function and print the result
print(expensesInQuarter(monthly_expenses))


# 3  Find out if you spent exactly 2000 dollars in any month
def checkAmountSpent(monthly_expenses):
    for i in monthly_expenses:
        if i == 2000:
                 
                 return True
        return False
print(checkAmountSpent(monthly_expenses))

















 


