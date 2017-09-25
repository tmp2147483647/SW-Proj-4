def factorial(n):
    n = int(input("n="))
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


def choose(n,k):
  if k==0:
     return 1
  elif n<k:
     return 0
  else:
     return choose(n-1, k-1) + choose(n-1, k)

def choose_iterative(n, k):
  stack = []
  stack.append((n, k))
  combinations = 0

  while len(stack):
    n, k = stack.pop()
    if k == 0:
      combinations += 1
    elif n<k:
      combinations += 0 #or just replace this line with `pass`
    else:
      stack.append((n-1, k))
      stack.append((n-1, k-1))

  return combinations 
