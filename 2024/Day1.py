import numpy as np 

def part1():

    # Text file data converted to integer data type 
    File_data = np.loadtxt(r"2024\Day1_input.txt", dtype=int) 
    print(File_data) 

    column0 = File_data[:,0]
    column1 = File_data[:,1]
    arrayLength = column0.size

    column0.sort()
    column1.sort()
    i=0
    distance =0
    for x in column0:
        y = column1[i]
        distance += abs(x-y)
        i+=1

    print(distance)


def part2():
    # Text file data converted to integer data type 
    File_data = np.loadtxt(r"2024\Day1_input.txt", dtype=int) 
    #print(File_data) 
    column0 = File_data[:,0]
    column1 = File_data[:,1]

    similarity = 0
    for x in column0:
        y = np.count_nonzero(column1 == x)
        print(x)
        print("similarity = "+str(y))
        similarity += x*y
    print(similarity)

def main():
    part1()   
    part2()

if __name__ == "__main__":
    main()