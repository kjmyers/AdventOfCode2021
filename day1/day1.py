


def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()
    
    previous = int(data[0].rstrip()) + int(data[1].rstrip()) + int(data[2].rstrip())
    print(previous, ' (N/A - no previous measurement)')
    #data = data[1:] #First reading removed

    increases = 0
    
    for ind in range(1,len(data)-2):
        depth = int(data[ind].rstrip()) + int(data[ind + 1].rstrip()) + int(data[ind + 2].rstrip())
        
        if( previous < depth ):
            increases += 1
            print(depth,' (increased), with increase: ', increases)
        else:
            print(depth, ' (decreased)')
    
        previous = depth

        depth = 0
        
    
    print('Total Increases: ', increases)
        


if __name__ == "__main__":
    main()