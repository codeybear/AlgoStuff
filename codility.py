from decimal import Decimal

def solution(S, B):
    amounts = []
    over = Decimal(S)
    output = []

    for num in B:
        amounts.append(Decimal(num))

    total = sum(amounts)

    for num in amounts:
        allocated = over * (num / total)
        allocated = round(allocated, 2)
        output.append(allocated)
        over = over - allocated
        total = total - num

    output = [str(num) for num in output]

    return output

print(solution('300.01', ['300.00', '200.00', '100.00']))


def solution(X):
    m = 60
    h = m * 60
    d = h *24
    w = d * 7
    output_count = 0
    output = ""

    if X // w > 0:
        output_count += 1
        output += f"{X // w}w"
        X = X % w

    if X // d > 0:
        output_count += 1
        output += f"{X // d}d"
        X = X % d


    if X // h > 0:
        output_count += 1
        output += f"{X // h}h"
        X = X % h

    if X // m > 0:
        output_count += 1

        if output_count == 2 and X % d > 0:
            X = X + m
            X = X - (X % m)

        output += f"{X // m}m"
        X = X % m

    if output_count <2:
        output += f"{X}s"

    return output



print(solution(7263))
