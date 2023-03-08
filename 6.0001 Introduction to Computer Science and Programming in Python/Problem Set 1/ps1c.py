# Constants
semi_annual_raise = 0.07
annual_investments_return = 0.04
portion_down_payment = 0.25
total_cost = 1_000_000
total_months = 36
down_payment_cost = total_cost * portion_down_payment

# User input variables
annual_salary = 0

# User enters data, cast them to floats
annual_salary = float(input('Enter the starting salary: '))

# Calculate savings with given rate
low = 0
high = 10000
savings_rate = (high + low)//2
bisection_search_steps = 0

result_found = False

while result_found == False:
    current_savings = 0
    current_month = 0

    # Convert annual_salary to monthly salary
    monthly_salary = annual_salary / 12

    bisection_search_steps += 1

    # Turn savings_rate into percentage (represented in decimal)
    savings_rate_percentage = savings_rate / 10_000

    # Calculate savings over 36 months
    for x in range(36):
        # Calculate monthly investment returns
        current_savings += current_savings * annual_investments_return / 12

        # Calculate monthly savings
        current_savings += monthly_salary * savings_rate_percentage

        # Increment months_amount
        current_month += 1

        # If months_amount is divideable by 6, raise monthly salary
        if current_month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise

    # Determine if result is satisfactory, in which case break loop
    if abs(current_savings - down_payment_cost) <= 100:
        result_found = True

        # Return result
        print(f'Best savings rate: {savings_rate / 10_000}')
        print(f'Steps in bisection search: {bisection_search_steps}')
        break
    elif savings_rate_percentage == 0.9999: # Check if it is even possible to save the required amount within 36 months (with highest savings rate)
        result_found = True
        print(f'It is not possible to pay the down payment in three years')
        break
    else:
        # Recalibrate low or high depending on result
        if (current_savings - down_payment_cost) > 100:
            high = savings_rate
        else:
            low = savings_rate
        
        # Redefine savings rate  
        savings_rate = (high + low)//2