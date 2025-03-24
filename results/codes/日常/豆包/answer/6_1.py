def merge_intervals(intervals):
    if not intervals:
        return []
    # 按区间的起始位置排序
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for interval in intervals[1:]:
        # 如果当前区间的起始位置小于等于前一个区间的结束位置
        if interval[0] <= merged[-1][1]:
            # 更新前一个区间的结束位置
            merged[-1] = (merged[-1][0], max(merged[-1][1], interval[1]))
        else:
            # 否则，将当前区间添加到结果中
            merged.append(interval)
    return merged


# 示例使用
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
print(merge_intervals(intervals))