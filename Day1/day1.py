
def sumTwo(inputList):
    for i in inputList:
        for k in inputList:
            if i == k:
                continue

            if i+k == 2020:
                return i*k

def sumThree(inputList):
    for i in inputList:
        for k in inputList:
            if i == k:
                continue
            for j in inputList:
                if j != k and j != i:
                    if i+k+j == 2020:
                        return i*k*j

def main():
    inputList = []
    with open('input.txt') as f:
        for line in f:
            inputList.append(int(line))
    
    val = sumTwo(inputList)
    print(val)

    val2 = sumThree(inputList)
    print(val2)

if __name__ == "__main__":
    main()