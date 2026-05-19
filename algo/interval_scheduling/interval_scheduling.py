
def interval_scheduling(intervals):    
    sorted_ivs = sorted(intervals, key=lambda x: x[1])
    
    selected = []
    last_end = float('-inf')
    
    for start, end in sorted_ivs:
        if start >= last_end:          # 不冲突
            selected.append((start, end))
            last_end = end
    
    return selected