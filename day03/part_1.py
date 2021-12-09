from collections import Counter


def main():
    diagnostics = []
    with open('input.txt') as f:
        diagnostics = list(map(str, f.read().splitlines()))

    gamma_rate = "".join(Counter(diagnostic[i] for diagnostic in diagnostics).most_common()[
                         0][0] for i in range(len(diagnostics[0])))
    epsilon_rate = "".join(Counter(diagnostic[i] for diagnostic in diagnostics).most_common(
    )[-1][0] for i in range(len(diagnostics[0])))

    gamm_rate_dec = int(gamma_rate, 2)
    epsilon_rate_dec = int(epsilon_rate, 2)

    power_consumption = gamm_rate_dec * epsilon_rate_dec

    print(f'The power consumption is {power_consumption}')


if __name__ == '__main__':
    main()
