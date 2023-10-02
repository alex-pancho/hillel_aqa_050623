def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
  # n=2 -> n=1    n=0

def fibonacci_sequence(n):
    if n <= 0:
        print("Invalid input! Please enter a positive integer.")
    else:
        return [fibonacci(i) for i in range(n)]


print("Fibonacci sequence:")
print(*fibonacci_sequence(17), sep=' ')
