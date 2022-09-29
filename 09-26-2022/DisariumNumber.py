

def disariumNumber(n):
    
    x = 1
    sum = 0
    for i in n:
        sum += int(i) ** x
        x += 1

    print('True') if int(n) == sum else print('False')
    
def main():
    n = input("Enter a number: ")
    disariumNumber(n)

if __name__ == "__main__":
    main()