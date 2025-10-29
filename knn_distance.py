import random

def knndistance(arr, q, k):
    distances = []
	
    for num in arr:
        distances.append((abs(num - q), num))
    
    target = k - 1
    low = 0
    high = len(distances) - 1

    while True:
        if low == high:
            return distances[low]
        
        pivot = partition(distances, low, high)
        
        if target == pivot:
            return distances[target]
        elif target < pivot:
            high = pivot - 1
        else:
            low = pivot + 1

def partition(pairs, low, high):
    p = random.randint(low, high)
    pairs[p], pairs[high] = pairs[high], pairs[p]
    
    value = pairs[high][0]
    
    i = low
    for j in range(low, high):
        if pairs[j][0] <= value:
            pairs[i], pairs[j] = pairs[j], pairs[i]
            i += 1
            
    pairs[i], pairs[high] = pairs[high], pairs[i]
    return i
