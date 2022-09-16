''' Merge overlapping intervals problem

Given a list of intervals, merge all the overlapping intervals to produce a list 
that has only mutually exclusive intervals.

https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743622133_21Unit

My code does it inplace, the example appends to a new array

This problem came up twice - with administrate and manypets
'''

def merge_intervals(sections):
    if len(sections) < 2: 
        return None

    # sort the sections in start position order
    sections.sort(key=lambda x: x[0])
    pos = 0

    while pos < len(sections) - 1:
        if len(sections) < 2:
            break

        # is the start of the next section behind the end of the current section
        if sections[pos + 1][0] < sections[pos][1]:
            start = sections[pos][0]
            end = max(sections[pos][1], sections[pos + 1][1])
            sections[pos] = (start, end)
            del sections[pos + 1]
        else:
            pos += 1

    return sections


print(merge_intervals([(6, 7), (2, 4), (5, 9), (15, 20), (14, 22)]))