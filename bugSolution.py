def function_with_uncommon_error(n):
    if n == 0:
        return 1 # Correct base case to avoid ZeroDivisionError
    elif n == 1:
        return 1 # Another base case to make the recursion work correctly
    else:
        return n / function_with_uncommon_error(n-1)

# Example usage (will not raise RecursionError):

try:
    result = function_with_uncommon_error(5)
    print(f"Result: {result}")
except RecursionError:
    print("A RecursionError occurred. Check your function for infinite recursion")
except ZeroDivisionError:
    print("A ZeroDivisionError occurred. Check input parameter") 