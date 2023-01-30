# Starting Out With Python 5th Edition: Chapter 12 - Exercise 5

def main():
    try:
        arr = []

        # Initialize an integer list
        while True:
            arr.append(int(input('Enter a number (q to quit): ')))
    except ValueError:
        # Calculate and display sum
        print(f'\nArray: {arr}\nSum of Elements: {get_sum(arr)}')
    except Exception:
        print(Exception)


# Function accepts a list as an argument and calculates sum of all elements
def get_sum(arr):
    # Base case
    if len(arr) == 1:
        return arr[0]
    # Recursive case
    else:
        return arr[0] + get_sum(arr[1:])


# Call the main function
if __name__ == '__main__':
    main()
