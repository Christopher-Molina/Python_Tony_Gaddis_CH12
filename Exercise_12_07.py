# Starting Out With Python 5th Edition: Chapter 12 - Exercise 7

def main():
    # Prompt user for number and exponent
    number = int(input('Enter a number to be raised: '))
    exponent = int(input('Enter the exponent: '))

    # Calculate and display number raised to exponent
    print(f'{number}^{exponent} = {power(number, exponent)}')


# Recursive power method
def power(number, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return number * exponent
    else:
        return number * power(number, exponent - 1)


# Call the main function
if __name__ == '__main__':
    main()
