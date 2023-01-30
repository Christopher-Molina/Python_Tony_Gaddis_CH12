# Starting Out With Python 5th Edition: Chapter 12 - Exercise 2

def main():
    # Input integer x and y
    x = int(input('Enter integer x: '))
    y = int(input('Enter integer y: '))

    # Calculate x times y
    result = multiply(x, y)

    # Display result
    print(f'{x} x {y} = {result}')


# Function returns product of x and y recursively
def multiply(x, y):
    if x == 0 or y == 0:  # Base case
        return 0
    else:  # Recursive case
        return x + multiply(x, y-1)


# Call the main function
if __name__ == '__main__':
    main()
