file1 = open('sampleData', 'r')
sample_data = file1.readlines()
print("size of sample_data list: " + str(len(sample_data)))

for x in sample_data:
    x = int(x)
    for y in sample_data:
        y = int(y)
        for z in sample_data:
            z = int(z)
            sum = x + y + z
            if sum == 2020:
                answer = x * y * z
                print("the answer is: " + str(answer))