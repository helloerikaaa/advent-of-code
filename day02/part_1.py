def main():
    commands = []
    with open('input.txt') as f:
        for line in f.readlines():
            key, value = line.split(' ')
            commands.append((key, int(value)))

    position = 0
    depth = 0
    
    for i in range(0, len(commands)):
        if commands[i][0] == 'forward':
            position += commands[i][1]
        elif commands[i][0] == 'up':
            depth -= commands[i][1]
        elif commands[i][0] == 'down':
            depth += commands[i][1]
    
    final_config = depth * position

    print(f'Final position and depth is {final_config}')


if __name__ == '__main__':
    main()
