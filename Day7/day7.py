from collections import defaultdict

def findParentBag(inputList, bagList):
    parentBag = set()
    for i in range(len(inputList)):
        for j in range(len(bagList)):
            if bagList[j] in inputList[i]:
                parentOfShinyParent = inputList[i].split(" ")
                parentColorOfShinyParent = parentOfShinyParent[0] + " " + parentOfShinyParent[1]

                if bagList[j] not in parentColorOfShinyParent:
                    parentBag.add(parentColorOfShinyParent)

    return list(parentBag)

def findBagPart1(inputList):
    bagContainsShinyGold = []
    for i in range(len(inputList)):
        if "shiny gold" in inputList[i]:
            parentBag = inputList[i].split(" ")

            parentBagColor = parentBag[0] + " " + parentBag[1]

            if "shiny gold" not in parentBagColor:
                bagContainsShinyGold.append(parentBagColor)

    #print(f'Bags that contain shiny gold: {bagContainsShinyGold}  length: {len(bagContainsShinyGold)}')

    allParent = set()
  
    parentBags = bagContainsShinyGold

    while True:
        bagContainsShinyGoldParentBag = [] 
        bagContainsShinyGoldParentBag = findParentBag(inputList, parentBags)

        #print(f'Found following parents: {bagContainsShinyGoldParentBag}\nLength: {len(bagContainsShinyGoldParentBag)}')
        if len(bagContainsShinyGoldParentBag) != 0:
            for i in bagContainsShinyGoldParentBag:
                allParent.add(i)
            parentBags = bagContainsShinyGoldParentBag
        else:
            break

    for i in bagContainsShinyGold:    
        allParent.add(i)

    #print(f'Bags that contain shiny gold parents: {list(allParent)} length: {len(allParent)}')

    return len(list(allParent))

def findPart2Result(startingColor, childBagsDict):
    total = 0
    for num, color in childBagsDict[startingColor]:
        total += int(num) + (int(num) * findPart2Result(color, childBagsDict))
    return total

def createParentChildDict(inputList):
    parentChildDict = defaultdict(list)
    for line in inputList:
        parent, childs = [token for token in line.split(' bags contain ')]
        #print(f'Parent: {parent}  Children: {childs}')

        for child in childs.replace('.', '').split(', '):
            if child != 'no other bags':
                num = int(child[0])
                ch = child[1:].split(' bag')[0].strip()
                parentChildDict[parent].append((num, ch))
    return parentChildDict
    
def main():
    inputList = []
    with open('input.txt') as f:
        val = f.read()
        for line in val.split(".\n"):
            inputList.append(line.replace("\n",""))

    result1 = findBagPart1(inputList)
    print(f'Part 1 - results: {result1}')

    parentChildDict = createParentChildDict(inputList)
    result2 = findPart2Result("shiny gold", parentChildDict)
    print(f'Part 2 - results: {result2}')

if __name__ == "__main__":
    main()