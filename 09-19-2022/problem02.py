

def sumOfAllDigits(T, string):
    sum = 0

    for i in string:
        if (i.isnumeric()):
            sum = sum + int(i)

    print(sum)

def main():
    T = input("Enter number of tests: ")
    string = input("Enter a Alpha-Numeric String: ")

    sumOfAllDigits(T, string)


if __name__ == "__main__":
    main()