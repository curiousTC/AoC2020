def findAccumulatorValuePart1(inputList):
    accumulator = 0
    index = 0
    traversed = set() #Track what indices we have covered
    
    while index < len(inputList):
        operation, increment = inputList[index].split(" ")

        if operation == 'acc': 
            accumulator += int(increment)
            index += 1
        elif operation == 'nop': 
            index += 1
        elif operation == 'jmp': 
            index += int(increment)

        if index in traversed: 
            break
        traversed.add(index)
    
    return accumulator

def findAccumulatorValuePart2(inputList):
    for i in range(len(inputList)): #Incrementally change either nop -> jmp or vice versa once, and iterate over new list
        #print(f'Before: {inputList}')
        changedList = list(inputList) # Reset back to original list
        operation, increment = changedList[i].split(" ")
        if operation == 'nop' and int(increment) != 0:
            changedList[i] = 'jmp ' + increment 
        elif operation == 'jmp':
            changedList[i] = 'nop ' + increment
        else:
            continue
        
        #print(f'After : {changedList}')
        result = findAccumulatorValueBasedOnList(changedList)
        if result == None:
            continue
        else:
            return result


def findAccumulatorValueBasedOnList(changedList):
    numOfTimes = 0 # Need this so that we can exit out of infinite loop
    accumulator = 0 
    index = 0
    while index < len(changedList) and numOfTimes < 500:
        operation, increment = changedList[index].split(" ")

        if operation == 'acc': 
            accumulator += int(increment)
            index += 1
        elif operation == 'nop': 
            index += 1
        elif operation == 'jmp': 
            index += int(increment)
        
        if index == len(changedList):
            return accumulator
        numOfTimes += 1

def main():
    inputList = []
    with open('input.txt') as f:
        for line in f:
            inputList.append(line.replace("\n",""))

    res = findAccumulatorValuePart1(inputList)
    print(f'Part 1 - Results: {res}')

    res2 = findAccumulatorValuePart2(inputList)
    print(f'Part 2 - Results: {res2}')

if __name__ == "__main__":
    main()