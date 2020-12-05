def isValid(passportString):
    """
    :param passport: string of a passport
    :return:boolean of whether valid
    >>> isValid('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')
    True
    >>> isValid('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929')
    False
    >>> isValid('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm')
    True
    >>> isValid('hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in')
    False
    """
    import re
    passport = makeMapFromString(passportString)
    if 'byr' in passport.keys():
        if not 1920 <= int(passport['byr']) <= 2002:
            return False
    else:
        return False

    if 'iyr' in passport.keys():
        if not 2010<=int(passport['iyr'])<=2020:
            return False
    else:
        return False

    if 'eyr' in passport.keys():
        if not 2020 <= int(passport['eyr']) <= 2030:
            return False
    else:
        return False

    if 'hgt' in passport.keys():
        heightString = passport['hgt']
        if "cm" in heightString:
            height = int(heightString.strip('cm'))
            if not 150 <= height <= 193:
                return False
        elif "in" in heightString:
            height = int(heightString.strip('in'))
            if not 59 <= height <= 76:
                return False
        else:
            return False
    else:
        return False

    hairColourPattern = '#[0-9a-f]{6}'
    hairColourRegex = re.compile(hairColourPattern)
    if 'hcl' in passport.keys():
        if not hairColourRegex.search(passport['hcl']):
            return False
    else:
        return False

    eyeColourPattern = 'amb|blu|brn|gry|grn|hzl|oth'
    eyeColourRegex = re.compile(eyeColourPattern)
    if 'ecl' in passport.keys():
        if not eyeColourRegex.search(passport['ecl']):
            return False
    else:
        return False

    idPattern = '[0-9]{9}'
    idRegex = re.compile(idPattern)
    if 'pid' in passport.keys():
        if not idRegex.search(passport['pid']):
            return False
    else:
        return False

    return True

def makeMapFromString(passportString):
    passportMap = {}
    fieldList = passportString.split(' ')
    for item in fieldList:
        itemList = item.split(':')
        key = itemList[0]
        value = itemList[1]
        passportMap[key] = value
    return passportMap

def parseArray(arrayOfLines):
    """
    :param arrayOfLines: ungrouped
    :return: array of passport lists
    >>> len(parseArray(getTestArray()))
    4
    >>> parseArray(getTestArray())[0]
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
    >>> parseArray(getTestArray())[1]
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
    >>> parseArray(getTestArray())[2]
    'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
    >>> parseArray(getTestArray())[3]
    'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'
    """
    arrayOfPassports = []
    lastPassportString = ""
    for line in arrayOfLines:
        if line == "\n":
            if lastPassportString != "":
                arrayOfPassports.append(lastPassportString.strip(' '))
                lastPassportString = ""
        else:
            lastPassportString += line.strip('\n')
            lastPassportString += ' '
    arrayOfPassports.append(lastPassportString.strip(' '))
    return arrayOfPassports

def run(sampleData):
    passportArray = parseArray(sampleData)
    counter = 0
    for passport in passportArray:
        if isValid(passport):
            counter += 1
    return counter

def getTestArray():
    file = open('testData', 'r')
    return file.readlines()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(run(sample_data)))
