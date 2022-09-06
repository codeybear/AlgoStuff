def MergeSort(a, b):
    aptr = bptr = 0
    c = [0] * (len(a) + len(b))

    while aptr < len(a) and bptr < len(b):
        if a[aptr] < b[bptr]:
            c[aptr + bptr] = a[aptr]
            aptr += 1
        else:
            c[aptr + bptr] = b[bptr]
            bptr += 1

    # this needs to be a loop to finish off, the quicksort examples seem to do this also
    if len(a) > len(b):
        c[aptr + bptr:len(c)] = a[bptr:len(a)]
    else:
        c[aptr + bptr:len(c)] = b[aptr:len(b)]

    return c

a = [1, 3, 5, 10, 20, 30, 40]
b = [2, 4, 8]

c = MergeSort(a, b)
print(c)
assert c == [1, 2, 3, 4, 5, 8, 10, 20, 30, 40]