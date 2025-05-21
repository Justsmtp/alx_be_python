#Users input
income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))

#calculate the monthly savings
monthly_savings = income - expenses

#projected annual savings
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#print output to display result
# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
