def passwordIsValid(rule, password):
    """
    Checks is a password meets a rule.

    >>> passwordIsValid('1-3 a', 'abcde')
    True
    >>> passwordIsValid('1-3 b', 'cdefg')
    False
    >>> passwordIsValid('2-9 c', 'ccccccccc')
    False
    >>> passwordIsValid('11-14 b', 'bkbxxdkrbzbswb')
    False
    >>> passwordIsValid('6-12 r', 'fhrrrtrrrcwg')
    False
    """

    ruleParts = rule.split(' ')
    targetLetter = ruleParts[1]
    range = ruleParts[0].split('-')
    firstPosition = int(range[0])-1
    secondPosition = int(range[1]) -1
    letters = list(password)
    found1 = False
    found2 = False
    if letters[firstPosition] == targetLetter:
        found1 = True
    if letters[secondPosition] == targetLetter:
        found2 = True
    if found1 == found2:
        return False
    else:
        return True



def getRulePasswordMapFromRow(row):
    """
    :param row: InputString
    :return: map {"rule":rule, "password":password}

    >>> getRulePasswordMapFromRow('1-3 a: abcde')['password']
    'abcde'
    >>> getRulePasswordMapFromRow('1-3 a: abcde')['rule']
    '1-3 a'
    """
    splitRow = row.split(':')
    rule = splitRow[0].strip()
    password = splitRow[1].strip()
    mapRulePass = dict(rule=rule, password=password)
    return mapRulePass

def iterateAndCheckList(listOfRows):
    """
    :param listOfRows:
    :return: a count of valid rows

    >>> iterateAndCheckList(['1-3 a: abcde','1-3 b: cdefg','2-9 c: ccccccccc'])
    1
    """
    counter = 0
    for row in listOfRows:
        map = getRulePasswordMapFromRow(row)
        valid = passwordIsValid(map['rule'], map['password'])
        if valid:
            counter+=1
    return counter


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file1 = open('sampleData', 'r')
    sample_data = file1.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(iterateAndCheckList(sample_data)))

