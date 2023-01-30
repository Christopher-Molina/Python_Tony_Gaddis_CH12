# Starting Out With Python 5th Edition: Chapter 12 - Exercise 6

def main():
    # Prompt user for an integer
    number = int(input('Enter a number: '))

    # Calculate and display the sum from 1 up to number
    print(f'The sum from 1 up to {number} is {sum(1, number)}')


# Function returns the sum from 1 up to number
def sum(start, number):
    if start == number:  # Base case
        return number
    else:  # Recursive case
        return start + sum(start + 1, number)


# Call the main function
if __name__ == '__main__':
    main()
