import argparse

def lcs(x: str, y: str) -> int:
    #declare an array to store memo values
    memo = [[None] * (len(y) + 1) for i in range(len(x) + 1)]

    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == 0 or j == 0:
                memo[i][j] = 0
            elif x[i-1] == y[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

    return memo[len(x)][len(y)]

def ld(x: str, y: str) -> int:
    #declare an empty array called memo
    memo = [[None] * (len(y) + 1) for i in range(len(x) + 1)]

    for i in range(len(x) + 1):
        memo[i][0] = i
    for j in range(len(y) + 1):
        memo[0][j] = j

    first = 0
    second = 0
    third = 0

    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if (x[i-1] == y[j-1]):
                memo[i][j] = memo[i-1][j-1]
            else:
                first = memo[i][j-1]
                second = memo[i-1][j]
                third = memo[i-1][j-1]

                if(first <= second and first <= third):
                    memo[i][j] = first + 1
                elif(second <= first and second <= third):
                    memo[i][j] = second + 1
                else:
                    memo[i][j] = third + 1
    return memo[len(x)][len(y)]


def lps(x: str) -> int:
    def longest(x: str, i: int, j: int) -> int:
        if (i == j):
            return 1
        if (x[i] == x[j] and i + 1 == j):
            return 2
        if (x[i] == x[j]):
            return longest(x, i + 1, j - 1) + 2

        return max(longest(x, i, j - 1), longest(x, i + 1, j))

    return longest(x, 0, len(x) - 1)


def pmin(x: str) -> int:
    n = len(x)
    count = 0

    for i in range(n//2):
        if(x[i] == x[n-i-1]):
            continue
        count += 1
    return count

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--fn", type=str, default="all",
                        choices=["lcs", "ld", "lps", "pmin", "all"], help="Select the function you want to call "
                                                                          "('all' to run all functions)")
    parser.add_argument("--x", type=str, default="apple", help="String X")
    parser.add_argument("--y", type=str, default="place", help="String Y")
    args = parser.parse_args()

    x = args.x
    y = args.y
    fn = args.fn
    if fn in ["lcs", "all"]:
        print(f"LCS:\n\tX: {x}\n\tY: {y}\n\tLCS: {lcs(x, y)}")
    if fn in ["ld", "all"]:
        print(f"LD:\n\tX: {x}\n\tY: {y}\n\tLD: {ld(x, y)}")
    if fn in ["lps", "all"]:
        print(f"LPS:\n\tX: {x}\n\tLPS (x): {lps(x)}")
        if y:
            print(f"\tLPS (y): {lps(y)}")
    if fn in ["pmin", "all"]:
        print(f"PMin:\n\tX: {x}\n\tPMin (x): {pmin(x)}")
        if y:
            print(f"\nPMin (y): {pmin(y)}")
