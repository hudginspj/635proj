

def summarize(lst):
    counts = {}
    for item in lst:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    print(counts)

