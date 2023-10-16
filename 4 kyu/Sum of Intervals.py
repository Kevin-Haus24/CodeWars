# def sum_of_intervals(intervals):
#     sum_intervals = 0
#     list = []
#     for q in range(len(intervals)-1):
#         for w in range(q-1, len(intervals)):
#             if intervals[q][1] >= intervals[w][0] and intervals[q][0] <= intervals[w][1]:
#                 list += (min([intervals[q][0]], [intervals[w][0]]) + max([intervals[q][1]], [intervals[w][1]]))
#                 del intervals[q], intervals[w-1]
#                 intervals.append(list)
#
#     for i in intervals:
#         sum_intervals += i[1] - i[0]
#     return sum_intervals

#print(sum_of_intervals([(1, 5), (1, 5)]))
#print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))

def sum_of_intervals1(intervals):
    sum_intervals = 0
    merged_intervals = []
    for i in sorted(intervals):
        if not merged_intervals or merged_intervals[-1][1] < i[0]:
            merged_intervals.append(i)
        else:
            merged_intervals[-1] = (merged_intervals[-1][0], max(merged_intervals[-1][1], i[1]))

    for i in merged_intervals:
        sum_intervals += i[1] - i[0]
    return sum_intervals

print(sum_of_intervals1([(1, 5), (1, 5)]))
print(sum_of_intervals1([(0, 20), (-100_000_000, 10), (30, 40)]))