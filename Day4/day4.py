def findValidPassportPart1(inputList, reqFields):
    validPassport = 0

    for i in range(len(inputList)):
        passportFields = []
        
        for j in inputList[i].split(" "):
            entry = j.split(":")
            passportFields.append(entry[0])

        res = checkPassportFieldsValid(passportFields, reqFields)

        if res:
            validPassport += 1
    
    return validPassport

def findValidPassportPart2(inputList, reqFields):
    validPassport = 0

    for i in range(len(inputList)):
        passportFields = []
        passportValues = []
        validFieldValues = 0
        
        for j in inputList[i].split(" "):
            entry = j.split(":")

            passportFields.append(entry[0])
            passportValues.append(entry[1])

        res = checkPassportFieldsValid(passportFields, reqFields)
        
        if res: 
            for i in range(len(passportFields)):
                if passportFields[i] == 'cid':
                    continue
                elif passportFields[i] == 'byr':
                    if 1920 <= int(passportValues[i]) <= 2002:
                        validFieldValues += 1
                elif passportFields[i] == 'iyr':
                    if 2010 <= int(passportValues[i]) <= 2020:
                        validFieldValues += 1
                elif passportFields[i] == 'eyr':
                    if 2020 <= int(passportValues[i]) <= 2030:
                        validFieldValues += 1
                elif passportFields[i] == 'hgt':
                    if findValidHeight(passportValues[i]) == True:
                        validFieldValues += 1
                elif passportFields[i] == 'hcl':
                    if findValidHairColor(passportValues[i]) == True:
                        validFieldValues += 1
                elif passportFields[i] == 'ecl':
                    if findValidEyeColor(passportValues[i]) == True:
                        validFieldValues += 1
                elif passportFields[i] == 'pid':
                    if findValidPID(passportValues[i]) == True:
                        validFieldValues += 1

        if validFieldValues == len(reqFields): 
            validPassport += 1

    return validPassport

def findValidHeight(height):
    h = ""
    for i in range(len(height)):
        if height[i].isdigit():
            h += height[i]

    if "cm" in height and (150 <= int(h) <= 193):
        return True
    if "in" in height and (59 <= int(h) <= 76):
        return True

    return False

def findValidPID(pid):
    if len(pid) != 9:
        return False
    if pid.isnumeric():
        return True
    return False

def findValidEyeColor(ecl):
    validEyeColor = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    if ecl in validEyeColor:
        return True
    return False

def findValidHairColor(hcl):
    if hcl[0] != "#":
        return False
    if len(hcl) != 7:
        return False
    
    validHcl = 0
    for i in range(1, len(hcl)):
        if hcl[i].isalpha() or hcl[i].isnumeric():
            validHcl += 1

    if validHcl == (len(hcl) - 1):
        return True

    return False

def checkPassportFieldsValid(passportFields, reqFields):
    validFields = 0
    for ele in passportFields:
        if ele == 'cid':
            continue
        if ele in reqFields:
            validFields += 1

    if validFields == len(reqFields):
        return True        

def main():
    reqFields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid'
    ]

    inputList = []
    with open('input.txt') as f:
        val = f.read()
        for line in val.split("\n\n"):
            inputList.append(line.replace("\n"," "))

    result = findValidPassportPart1(inputList, reqFields)
    print(f'Part 1 - Valid Passports: {result}')

    result2 = findValidPassportPart2(inputList, reqFields)
    print(f'Part 2 - Valid Passports: {result2}')

if __name__ == "__main__":
    main()