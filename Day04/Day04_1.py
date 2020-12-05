def isValid(passport):
    """
    :param passport: string of a passport
    :return:boolean of whether valid
    >>> isValid('ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm')
    True
    >>> isValid('iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929')
    False
    >>> isValid('hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm')
    True
    >>> isValid('hcl:#cfa07d eyr:2025 pid:166559648iyr:2011 ecl:brn hgt:59in')
    False
    """
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passportMap = makeMapFromString(passport)
    counter = 0
    for key in keys:
        if key in passportMap:
            counter += 1
    if counter == len(keys):
        return True
    else:
        return False

def makeMapFromString(passportString):
    passportMap = {}
    fieldList = passportString.split(' ')
    for item in fieldList:
        itemList = item.split(':')
        key = itemList[0]
        value = itemList[1]
        passportMap[key] = value
    return passportMap


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    # TODO needs a dunction to take white space separated arbitrary multiline info and turn into an array of strings
    # print("the answer is: " + str(run(sample_data)))
