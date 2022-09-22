

def secondMaxOfTriplet(N, tripletList):

    output = "Second max in Triplet: {} is {}"

    # iterate through the list of triplets list
    for list in tripletList:
        # sorting a list of 3 integer is not costly O(1)
        list.sort()
        secondMax = list[1]
        print(output.format(list, secondMax))
        


def main():

    flag = True
    list = []
    N = 0

    while flag:
        N = int(input("Enter Number of Triplet: "))
        if N >= 1 and N <= 6:
            flag = False
    
    for i in range(0, N):
        tripletStr = str(input())
        list.append([int(x) for x in tripletStr.split()])

    secondMaxOfTriplet(N, list)



if __name__ == "__main__":
    main()