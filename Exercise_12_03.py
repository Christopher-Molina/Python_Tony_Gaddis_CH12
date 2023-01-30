# Starting Out With Python 5th Edition: Chapter 12 - Exercise 3

def main():
    # Prompt user for integer argument n
    n = int(input('Enter an integer: '))

    # Display n lines of asterisks on the screen
    print(lines(1, n))


# Recursive function prints n lines of asterisks on the screen
def lines(start, end):
    if start == end:  # Base case
        return '*'
    else:  # Recursive case
        print('*')
        return lines(start+1, end)


# Call the main function
if __name__ == '__main__':
    main()
