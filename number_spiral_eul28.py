# https://www.educative.io/answers/how-to-solve-the-number-spiral-diagonals-problem
# No point figuring this out although I was right to look for patterns in
# you would spend a fair amount of time doing this though


def sum(dim):
    n = (dim - 1) / 2
    #find n
    # use the formula defined above
    x = (3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3
    return x


def main():
    # call the function and print the value
    diagonal = sum(101)
    print(diagonal)


main()
