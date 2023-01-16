import numpy

# Ask user to enter number x
print('Enter number x: ', end="")
x = input()

# Ask user to enter number y
print('Enter number y: ', end="")
y = input()

# Convert x and y to integers
x_integer = int(x)
y_integer = int(y)

# Print out x raised to the power of y
x_power_of_y = x_integer ** y_integer
print(f'X**y = {x_power_of_y}')

# Calculate log (base 2) of x
log_2_of_x = numpy.log2(x_integer)

# Print log (base 2) of x
int_log_2_of_x = int(log_2_of_x)
print(f'log(x) = {int_log_2_of_x}')