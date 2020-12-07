def run(data):
    """
    :param data:
    :return:
    >>> run([])
    None
    """
    highestID = 0
    for seat in data:
        thisID = calculateID(seat)
        if thisID > highestID:
            highestID = thisID
    return highestID

def calculateID(seatTag):
    """
    :param seatTag:
    :return:
    >>> calculateID('BFFFBBFRRR')
    567
    >>> calculateID('FFFBBBFRRR')
    119
    >>> calculateID('BBFFBBFRLL')
    820
    """
    rowTag = seatTag[:7]
    aisleTag= seatTag[7:]
    row = findPos(127, 'F', rowTag)
    seatPosition = findPos(7, 'L', aisleTag)
    id = row * 8 + seatPosition
    return id

def findPos(highest, firstHalfChar, CharList):
    """
    :param highest:
    :param firstHalfChar:
    :param CharList:
    :return:
    >>> findPos(127, 'F', 'BFFFBBF')
    70
    >>> findPos(7, 'L', 'RLR')
    5
    >>> findPos(7, 'L', 'RRR')
    7
    """
    max = highest
    lowest = 0
    for char in CharList:
        if(char == firstHalfChar):
            highest = (lowest + highest) // 2
        else:
            lowest = (highest - lowest) // 2 + lowest + 1

    if(highest==lowest):
        return highest
    else:
        return 'fucked'

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file = open('sampleData', 'r')
    sample_data = file.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(run(sample_data)))