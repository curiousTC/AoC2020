# Create a new map that has a specified pattern duplicated n times
def createNewMap(map, n): 
    newMap = []
    for p in map:
        newMap.append(p*n)
    return newMap

def countTrees(map, right, down):
    numberOfTrees = 0
    x = 0
    y = 0

    height = len(map)

    while y < height:
        if map[y][x] == '#':
            numberOfTrees += 1
        x = x + right
        y += down
    
    return numberOfTrees

def main():
    map = []
    with open('input.txt') as f:
        for line in f:
            map.append(line.replace("\n",""))

    extended_map = createNewMap(map, 100) #increase the n value if running into index out of range error so that map is large enough to traverse

    numOfTrees = countTrees(extended_map, 3, 1)
    print(f'Part 1: {numOfTrees}')

    val1 = countTrees(extended_map, 1, 1)
    val2 = countTrees(extended_map, 3, 1)
    val3 = countTrees(extended_map, 5, 1)
    val4 = countTrees(extended_map, 7, 1)
    val5 = countTrees(extended_map, 1, 2)

    product = val1 * val2 * val3 * val4 * val5
    print(f'Part 2: {product}')

if __name__ == "__main__":
    main()