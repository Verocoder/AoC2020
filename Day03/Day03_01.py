
def runSubtraction(data):
    """
    :param data: tree map,1 uniqueness wide
    :return: count of trees hit
    >>> runSubtraction(getTestData())
    7
    """
    countTrees = 0
    countX = 0
    for line in data:
        lineList = list(line)
        lineLen = len(lineList) - 1
        # check to see if gone off side of map and move back one map width if so
        if(countX >= lineLen):
            countX -= lineLen
        if(line[countX]) == "#":
            countTrees += 1
        countX += 3

    return countTrees


def runDivision(data):
    """
    :param data: tree map,1 uniqueness wide
    :return: count of trees hit
    >>> runDivision(getTestData())
    7
    """
    countTrees = 0
    countX = 0
    countY = 0
    for line in data:
        lineLen = len(line)
        # ??????
        # check to see if gone off side of map and move back one map width if so
        if(countX > lineLen):
            countX -= lineLen
        if(line[countX]) == "#":
            countTrees += 1
        countX += 3

    return countTrees

def getTestData():
    file = open('testData', 'r')
    return file.readlines()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(run(sample_data)))
