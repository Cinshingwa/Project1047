

# tax rate 20%
TAX = 0.20

# Deduction $10,000
standard_deducation = 10000

# Additional Deduction $3,000 per dependent
dependent = 3000

# Gross income must be to nearest penny: $150,000.00
gross_income = float(input("Enter gross income: "))

# Number of Dependents: 3
number_dependents = int(input("Enter the number of dependents: ")) * dependent

# income tax is
income_tax = (((gross_income - standard_deducation)-number_dependents) * TAX)

# answer round to penny amount
IncomeTax = round(income_tax,2)
print("Your income tax is $", IncomeTax)









