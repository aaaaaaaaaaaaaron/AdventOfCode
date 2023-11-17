# opening the file in read mode 
my_file = open("AdventOfCode\\2022\\1\input.txt", "r") 
  
# reading the file 
data = my_file.read() 




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
    caloryCount.sort()
    print(caloryCount[-1])

            #caloryCount[1] = line
        # # Remove the newline character at the end of the line
        # line = line.strip()

        # # Append the line to the list
        # lines.append(line)

# Print the list of lines
