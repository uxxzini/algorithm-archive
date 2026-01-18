from collections import Counter

def solution(array):
    count = Counter(array)
    
    max_freq = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_freq]
    
    return modes[0] if len(modes) == 1 else -1
