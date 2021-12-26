def main():
    with open('input.txt', 'r') as file:
        data = file.readlines()
    
    depth = 0
    hoz = 0

    for line in data:

        command, change_str = line.split(' ')
        change = int(change_str)

        match command:
            case 'up' :
                depth += change
            case 'down':
                depth -= change
            case 'forward':
                hoz += change
        print(line.strip())
        print('depth:',depth)
        print('horizontal:',hoz)
    print(depth * hoz)


if __name__ == "__main__":
    main()