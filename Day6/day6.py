import string

def findAnswersPart1(inputList):
    answeredYes = 0

    for i in range(len(inputList)):
        answer = list(set(inputList[i]))
        answeredYes += len(answer)
    
    return answeredYes

def findAnswersPart2(inputList):
    answeredYes = 0

    for i in range(len(inputList)):
        if ',' not in inputList[i]: 
            answeredYes += len(inputList[i])
            continue

        individual = inputList[i].split(",")

        foundMatch = set()
        for k in range(len(inputList[i])): 
            count = 0
            for j in range(len(individual)):
                if inputList[i][k] in individual[j]:
                    count += 1

                if count == len(individual):
                    foundMatch.add(inputList[i][k])

        answeredYes += len(foundMatch)

    return answeredYes

def main():
    inputList = []
    individual = []
    with open('input.txt') as f:
        val = f.read()
        for line in val.split("\n\n"):
            inputList.append(line.replace("\n",""))
        for line in val.split("\n\n"):
            individual.append(line.replace("\n",",")) #Separate each individual's answers with a delimeter per group

    result1 = findAnswersPart1(inputList)
    print(f'Part 1 - Answered yes total: {result1}')

    result2 = findAnswersPart2(individual)
    print(f'Part 2 - Results: {result2}')

if __name__ == "__main__":
    main()