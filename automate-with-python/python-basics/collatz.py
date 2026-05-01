# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result

# Then, write a program that lets the user enter an integer
# and that keeps calling collatz() on that number
# until the function returns the value 1.

try:
    number_input = int(input('Enter number: '))
    # Keep calling the function until it reaches 1
    while number_input != 1:
        number_input = collatz(number_input)
except ValueError:
    print('Enter a valid integer please')
