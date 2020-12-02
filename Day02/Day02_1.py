def passwordIsValid(rule, password):
    """
    Checks is a password meets a rule.

    >>> passwordIsValid('1-3 a', 'abcde')
    True
    >>> passwordIsValid('1-3 b', 'cdefg')
    False
    >>> passwordIsValid('2-9 c', 'ccccccccc')
    True
    """
    import re

    ruleParts = rule.split(' ')
    regexString = '[' + ruleParts[1] + ']{' + ruleParts[0].replace('-',',') + '}'
    valid = re.search(regexString, password)
    if valid:
        return True
    else:
        return False


def getRulePasswordMapFromRow(row):
    """
    :param row: InputString
    :return: map {"rule":rule, "password"}

    >>> getRulePasswordMapFromRow('1-3 a : abcde')['password']
    'abcde'
    >>> getRulePasswordMapFromRow('1-3 a : abcde')['rule']
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
    2
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