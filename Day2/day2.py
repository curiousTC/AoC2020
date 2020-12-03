def findValidPassword(inputList):
    validPw = 0

    for line in inputList:
        val = line.replace(":"," ").split()
        #print(f'Password policy: {val[0]}, character: {val[1]}, password: {val[2]}')

        countChar = 0
        for char in val[2]:
            if char == val[1]:
                countChar += 1
        
        policy = val[0].replace("-", " ").split()
        minCharCount = int(policy[0])
        maxCharCount = int(policy[1])

     
        if minCharCount <= countChar <= maxCharCount:
            validPw += 1
    
    return validPw

def findValidPasswordBasedOnCharPositions(inputList):
    validPw = 0

    for line in inputList:
        val = line.replace(":"," ").split()
        # print(f'Password policy: {val[0]}, character: {val[1]}, password: {val[2]}')
        
        policy = val[0].replace("-", " ").split()
        validCharPos1 = int(policy[0]) - 1 
        validCharPos2 = int(policy[1]) - 1

        password = list(val[2])
        char = val[1]

        posList = []
        for i in range(len(password)):
            if (i == validCharPos1 and password[i] == char) or (i == validCharPos2 and password[i] == char):
                posList.append(i)
            
        if len(posList) == 1:
            validPw += 1

    return validPw
        
def main():
    inputList = []
    with open('input.txt') as f:
        for line in f:
            inputList.append(line.replace("\n"," "))

    validPw = findValidPassword(inputList)
    print(f'Part 1 - Valid Passwords: {validPw}')

    validPws = findValidPasswordBasedOnCharPositions(inputList)
    print(f'Part 2 - Valid Passwords: {validPws}')
    


if __name__ == "__main__":
    main()