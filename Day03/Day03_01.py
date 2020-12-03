def getTestData():
    file = open('testData', 'r')
    return file.readlines()

def run(data):
    """
    :param data: tree map,1 uniqueness wide
    :return: count of trees hit
    >>> run(getTestData())
    7
    """
    countTrees = 0
    countX = 0
    for line in data:
        lineList = list(line)
        lineLen = len(line) -1
        while(countX > lineLen):
            countX -= lineLen
        if(line[countX]) == "#":
            countTrees += 1
        countX += 3

    return countTrees

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(run(sample_data)))
