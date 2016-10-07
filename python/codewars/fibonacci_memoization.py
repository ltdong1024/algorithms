'''
  Memoization refers to remember results of previous method calls in order to avoid unnecessary repeated computations.
  
  Three cases: simple one (cache is public), private cache version (detailed) and succint private cache
'''

# simple one (public cache)

fibonacci_memo = {0: 0, 1: 1}
def fibonacci_public(n):
    if n in [0, 1]:
        return n
    if n not in fib_memo:
        fib_memo[n] = fibonacci_public(n-1) + fibonacci_public(n-2)
    return fib_memo[n-1] + fib_memo[n-2]


# private cache
def fibonacci_private(n, fib_memo=None):
    if n in [0, 1]:
        return n
    if fib_memo is None:
    	fib_memo = { 0: 0, 1: 1}
    if n not in fib_memo:
        fib_memo[n] = fibonacci_private(n-1, fib_memo) + fibonacci_private(n-2, fib_memo)
    return fib_memo[n-1] + fib_memo[n-2]
    
# private cache (succint)
def fibonacci(n, fib_memo = {0: 0, 1: 1}):
    if n not in prev:
        fib_memo[n] = fibonacci(n-1, fib_memo) + fibonacci(n-2, fib_memo)
    return fib_memo[n]
    
