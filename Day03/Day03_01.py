
def runSubtraction(data):
    """
    :param data: tree map,1 uniqueness wide
    :return: count of trees hit
    >>> runSubtraction(getTestData())
    7
    """
    countTrees = 0
    countX = 0
    countY = 0
    for line in data:
        lineList = list(line.strip('\n'))
        lineLen = len(lineList)
        # check to see if gone off side of map and move back one map width if so
        if(countX >= lineLen):
            countX -= lineLen

        # print(str(countX) + ',' + str(countY))
        if(line[countX]) == "#":
            countTrees += 1
        countX += 3
        countY +=1

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
    print("the answer is: " + str(runSubtraction(sample_data)))
