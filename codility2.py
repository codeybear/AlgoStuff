from decimal import Decimal
import math

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
        # allocated = math.floor(allocated * 100)/100.0
        output.append(allocated)
        over = over - allocated
        total = total - num

    output = [str(num) for num in output]

    return output

    # print(over, sum(amounts))

print(solution('300.01', ['300.00', '200.00', '100.00']))