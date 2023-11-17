with open("AdventOfCode\\2022\\1\input.txt", 'r') as file:
    # Create an empty list to store the lines
    lines = []
    caloryCount =[]
    counter = 0
    caloryCounter=0
    # Iterate over the lines of the file
    for line in file:

        if line not in ['\n', '\r\n']:
            caloryCounter +=int(line)
        else:
            caloryCount.append(caloryCounter)
            caloryCounter = 0
file.close

caloryCount.sort()
print(caloryCount[-1])
