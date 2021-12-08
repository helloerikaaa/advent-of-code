def main():
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            lines.append(int(line))

    current_window = sum(lines[0:3])
    counter = 0
    for i in range(1, len(lines) - 3 + 1):
        prev_window = current_window
        current_window = sum(lines[i:i+3])

        if current_window > prev_window:
            counter += 1

    print(f'There are {counter} increases')


if __name__ == '__main__':
    main()
