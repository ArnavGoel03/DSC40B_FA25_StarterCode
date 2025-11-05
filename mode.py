def mode(numbers):
  counts={}
  for num in numbers :
    if num in counts :
      counts[num]+=1
    else :
      counts[num]=1
  return max(counts,key=counts.get)
    
