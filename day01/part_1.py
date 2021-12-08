def main():
    lines = []
    with open('input.txt') as f:
        for line in f.readlines():
            lines.append(int(line))

    counter = sum(lines[i] > lines[i - 1] for i in range(1, len(lines)))

    print(f'There are {counter} increases')


if __name__ == '__main__':
    main()
