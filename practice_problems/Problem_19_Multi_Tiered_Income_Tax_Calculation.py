# Problem 19 - Multi-Tiered Income Tax Calculation
"""
Practice Problem: Calculate income tax for a given income based on these rules:

First $10,000: 0% tax
Next $10,000: 10% tax
Remaining income: 20% tax
Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

Given Input: income = 45000
"""

income = 45000
tax_payable = 0
print("Given income:", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # Tax on first 10k is 0. Tax on the rest is 10%
    tax_payable = (income - 10000) * 10 / 100
else:
    # First 10,000 (0% tax)
    # Next 10,000 (10% tax = 1,000)
    tax_payable = 0 + (10000 * 10 / 100) 
    # Remaining income (20% tax)
    tax_payable += (income - 20000) * 20 / 100

print("Total income tax to pay is", tax_payable)

"""
Explanation to Solution:

Cumulative Logic: The code doesn’t just check one condition; it accounts for every bracket the income “passes through.”
elif chain: This ensures that only the relevant calculation block is executed based on the total income range.
Mathematical Precision: By breaking the calculation into steps, you avoid the common mistake of taxing the entire 45,000 at the highest rate.
"""