# Returns a string list representation of FizzBuzz from 1 to n
return ["FizzBuzz" if i%15==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range (1,n+1)]

# Non list comprehension solution
""" retlist = []
for i in range(1, n):
    if i % 15 == 0:
        retlist.append("FizzBuzz")
    elif i % 3 == 0:
        retlist.append("Fizz")
    elif i % 5 == 0:
        retlist.append("Buzz")
    else:
        retlist.append(str(i))
return retlist """