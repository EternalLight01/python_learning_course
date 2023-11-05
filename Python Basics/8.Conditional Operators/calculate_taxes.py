# from UAH 1, 001 to UAH 10, 000 inclusive — tax of 3 % of income
# Create a function calculate_taxes that takes an integer income(your income) and returns the tax you will pay. 
# The amount of tax depends on your income:
# up to UAH 1, 000 inclusive — tax of 2 % of income
# more than UAH 10, 000 — tax of 5 % of income.
# Example:
# calculate_taxes(900)  # 18 (900 * 0.02)
# calculate_taxes(5000)  # 150 (5000 * 0.03)
# calculate_taxes(10500)  # 525 (10500 * 0.05)

def calculate_taxes(income: int) -> float:

    if income <= 1000:
        return income*0.02

    elif 1001 <= income <= 10000:
        return income*0.03

    elif income > 10000:
        return income*0.05

