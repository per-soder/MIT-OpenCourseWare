# Constants
portion_down_payment = 0.25
investments_return = 0.04

# User input variables
total_cost = 0
annual_salary = 0
portion_saved = 0
semi_annual_raise = 0

# User enters data, cast them to floats
annual_salary = float(input('Enter your annual salary: '))

portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

total_cost = float(input('Enter the cost of your dream home: '))

semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

# Calculate number of months until sufficient saving
current_savings = 0
months_amount = 0

while current_savings < (total_cost * portion_down_payment):
    # Calculate monthly investment returns
    current_savings += current_savings * investments_return / 12

    # Calculate monthly savings
    current_savings += annual_salary / 12 * portion_saved

    # Increment months_amount
    months_amount += 1

    # If months_amount is divideable by 6, raise annual salary
    if months_amount % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

# Return result
print(f'Number of months: {months_amount}')