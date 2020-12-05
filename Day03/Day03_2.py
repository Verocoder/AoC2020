
def run(data, offsetX, offsetY):
    """
    :param data: tree map,1 uniqueness wide
    :return: count of trees hit
    >>> run(getTestData(),3,1)
    7
    """
    countTrees = 0
    countX = 0
    countY = 0
    while countY < len(data):
        line = data[countY]
        lineList = list(line.strip('\n'))
        lineLen = len(lineList)
        # check to see if gone off side of map and move back one map width if so
        if(countX >= lineLen):
            countX -= lineLen
        # print(str(countX) + ',' + str(countY))
        if(line[countX]) == "#":
            countTrees += 1
        countX += offsetX
        countY += offsetY

    return countTrees


def getTestData():
    file = open('testData', 'r')
    return file.readlines()

def runMany(sampleData):
    first = run(sample_data, 1, 1)
    second = run(sample_data, 3, 1)
    third = run(sample_data, 5, 1)
    fourth = run(sample_data, 7, 1)
    fifth = run(sample_data, 1, 2)
    return first*second*third*fourth*fifth

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    # print("the answer is: " + str(run(sample_data, 1, 1)))
    # print("the answer is: " + str(run(sample_data, 3, 1)))
    # print("the answer is: " + str(run(sample_data, 5, 1)))
    # print("the answer is: " + str(run(sample_data, 7, 1)))
    # print("the answer is: " + str(run(sample_data, 1, 2)))
    print("the answer is: " + str(runMany(sample_data)))
