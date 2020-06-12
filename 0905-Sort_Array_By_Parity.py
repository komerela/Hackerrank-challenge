# Returns a string list representation of FizzBuzz from 1 to n
B = []
[B.append(x) for x in A if x%2 == 0]
[B.append(x) for x in A if x%2 != 0]
return B