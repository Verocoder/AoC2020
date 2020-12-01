
def solveArray(sample_data):
    """Return the factorial of n, an exact integer >= 0.

    >>> solveArray([979, 366, 675, 123, 456])
    241861950
    >>> solveArray([366, 675, 123, 456])

    """
    for x in sample_data:
        x = int(x)
        for y in sample_data:
            y = int(y)
            for z in sample_data:
                z = int(z)
                sum = x + y + z
                if sum == 2020:
                    answer = x * y * z
                    return answer
    return None



if __name__ == "__main__":
    import doctest
    doctest.testmod()

    file1 = open('sampleData', 'r')
    sample_data = file1.readlines()
    print("size of sample_data list: " + str(len(sample_data)))
    print("the answer is: " + str(solveArray(sample_data)))