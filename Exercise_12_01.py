# Starting Out With Python 5th Edition: Chapter 12 - Exercise 1

def main():
    # Prompt user for an integer
    n = int(input('Enter an integer: '))

    # Display numbers from 1 up to n
    display(1, n)


def display(start, end):
    if start == end:
        print(end)
    else:
        print(start)
        display(start+1, end)


# Call the main function
if __name__ == '__main__':
    main()
