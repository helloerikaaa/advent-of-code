def main():
    commands = []
    with open('input.txt') as f:
        for line in f.readlines():
            key, value = line.split(' ')
            commands.append({key: int(value)})

    position = sum(command['forward']
                   for command in commands if command.get('forward'))
    depth_down = sum(command['down']
                     for command in commands if command.get('down'))
    depth_up = sum(command['up'] for command in commands if command.get('up'))

    final_depth = depth_down - depth_up

    final = position * final_depth

    print(f'Final position and depth is {final}')


if __name__ == '__main__':
    main()
