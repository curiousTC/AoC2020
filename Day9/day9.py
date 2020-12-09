def findInvalidXMASPart1(inputList, preamble):
    for i in range(preamble, len(inputList)):
        prev = list(inputList[i-preamble:i])

        sumVal = 0
        validSum = set()
        target = int(inputList[i])
        for j in range(len(prev)):
            for k in range(len(prev)):
                if prev[j] != prev[k]:
                    sumVal = int(prev[j]) + int(prev[k])
                    if sumVal == target:
                        validSum.add(sumVal)
                    elif sumVal != target:
                        continue
        
        if not validSum:
            return target

def findEncryptionWeakness(inputList, target):
    result = 0
    for i in range(len(inputList)):
        for j in range(i, len(inputList)):
            subList = [int(v) for v in inputList[i:j]]
            if sum(subList) > target:
                break
            if sum(subList) == target: 
                result = min(subList) + max(subList)

                return result

    return target
                    
def main():
    inputList = []
    with open('input.txt') as f:
        for line in f:
            inputList.append(line.replace("\n",""))
    
    #print(inputList)

    res = findInvalidXMASPart1(inputList, 25)
    print(f'Part 1 - Results: {res}')

    res2 = findEncryptionWeakness(inputList, res)
    print(f'Part 2 - Results: {res2}')

if __name__ == "__main__":
    main()