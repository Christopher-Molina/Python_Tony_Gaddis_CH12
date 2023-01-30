# Starting Out With Python 5th Edition: Chapter 12 - Exercise 8

def main():
    try:
        m = int(input('Enter m: '))
        n = int(input('Enter n: '))

        print(f'Value of Ackermann({m}, {n}): {ackermann(m, n)}')
    except (RecursionError, TypeError, Exception) as e:
        print(e)


# Ackermann function
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# Call the main function
if __name__ == '__main__':
    main()
