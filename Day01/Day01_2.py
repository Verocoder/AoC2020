def solveArray(sample_data):
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

def test1():
    answer = solveArray([979, 366, 675,123, 456])
    if answer == 241861950:
        print("test 1 pass")
    else:
        print("test 1 fail")

def test2():
    answer = solveArray([366, 675,123, 456])
    if answer == 241861950:
        print("test 2 fail")
    else:
        print("test 2 pass")

test1()
test2()

file1 = open('sampleData', 'r')
sample_data = file1.readlines()
print("size of sample_data list: " + str(len(sample_data)))
print("the answer is: " + str(solveArray(sample_data)))