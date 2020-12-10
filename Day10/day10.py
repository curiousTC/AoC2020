def findJoltDifferenceProduct(inputList):
    product = 0
    one_jolt = 0
    three_jolt = 0

    for i in range(len(inputList)-1):
        if inputList[i+1] - inputList[i] == 1:
            one_jolt += 1
        elif inputList[i+1] - inputList[i] == 3:
            three_jolt += 1

    if inputList[0] == 1:
        one_jolt += 1

    print(f'OneJolt: {one_jolt}  ThreeJolt: {three_jolt}')
    product = one_jolt * three_jolt
    return product

def findDistinctOptions(inputList):
    totalComb = 0
    return totalComb

def main():
    inputList = []
    with open('test2.txt') as f:
        for line in f:
            inputList.append(int(line))
    inputList.sort()
    inputList.append(inputList[-1] + 3)
    #print(inputList)

    res = findJoltDifferenceProduct(inputList)
    print(f'Part 1 - Results: {res}')

    # res2 = findDistinctOptions(inputList)
    # print(f'Part 2 - Results: {res2}')


if __name__ == "__main__":
    main()