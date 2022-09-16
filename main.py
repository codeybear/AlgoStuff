from heapq import merge


def merge_intervals(sections):
    if len(sections) < 2: 
        return None

    sections.sort(key=lambda x: x[0])

    isOverlap = True
    pos = 0

    while isOverlap:
        if len(sections) < 2:
            break

        # is the start of the next section behind the end of the current section
        if sections[pos + 1][0] < sections[pos][1]:
            isOverlap = True
            start = min(sections[pos][0], sections[pos + 1][0])
            end = max(sections[pos][1], sections[pos + 1][1])
            sections[pos] = (start, end)
            del sections[pos + 1]
        else:
            isOverlap = False

    return sections


# print(merge_intervals([(1, 4), (2, 5), (7, 9)]))
# print(merge_intervals([(1, 4), (2, 6), (3, 5)]))
print(merge_intervals([(6, 7), (2, 4), (5, 9)]))