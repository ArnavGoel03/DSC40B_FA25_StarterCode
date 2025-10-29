import random

def knn_distance(arr, q, k):
    if k>len(arr):
        return None
    distance=[]
    for num in arr  :
        distance.append((abs(q-num),num))
    
        
    
    return None
