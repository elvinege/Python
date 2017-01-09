def recursivelyFact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * recursivelyFact(n-1)

print(recursivelyFact(5))
print(recursivelyFact(4))
print(recursivelyFact(1))
print(recursivelyFact(2))
print(recursivelyFact(0))
print(recursivelyFact(10))

def iterativelyFact(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, (n+1)):
            fact = fact * i
        return fact

print(iterativelyFact(0))
print(iterativelyFact(1))
print(iterativelyFact(2))
print(iterativelyFact(3))
print(iterativelyFact(4))
print(iterativelyFact(5))
