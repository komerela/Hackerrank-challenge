input: [1, 5, 3, 4, 8, 1, 7, 2]
output: 5
reason: longest consecutive array is [1, 5, 3, 4, 2]

1 1 2 3 4 5 7 8

input = {}
is 1 in map
is 1 + 1 in map
is 1 -1 in map

cache = {}
for i in unsortedArray:
  if i in cache:
    continue
    
  if i+1 in cache:
    forward = cache[i+1]
  
  if i-1 in cache:
    backward = cache[i-1]
  
  total = forward + backward + 1
  cache[i-backward] = total
  cache[i+forward] = total
  cache[i] = total
input['1'] 