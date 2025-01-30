def function_with_uncommon_error(n):
    if n == 0:
        return 0  #This return statement is missing in original code and will cause exception if n=0
    else:
        return n / function_with_uncommon_error(n-1)

# Example usage (will raise RecursionError if not handled):
#print(function_with_uncommon_error(5)) 

# Example with error handling
try:
    result = function_with_uncommon_error(5)
    print(f"Result: {result}")
except RecursionError:
    print("A RecursionError occurred. Check your function for infinite recursion")
except ZeroDivisionError:
    print("A ZeroDivisionError occurred. Check input parameter")