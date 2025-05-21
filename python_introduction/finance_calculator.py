#Users input
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

#calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

#projected annual savings
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print output to display result
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
