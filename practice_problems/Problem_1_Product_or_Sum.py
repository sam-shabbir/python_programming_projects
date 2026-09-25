def prod_or_sum(a, b):

    # FIX: `a is int` asks "is a the int type itself?" (always False for 20).
    # isinstance() asks "is a an int value?", which is what we want.
    if isinstance(a, int) and isinstance(b, int):
        prod = a*b
        total = a+b  # FIX: renamed from `sum` so it doesn't hide the built-in sum() function

        if prod <= 1000:
            return prod
        else:
            return total
    else:
        print('Please enter 2 integers!')

# Testing Case 1
result = prod_or_sum(20, 30)
print("The result is", result)

# Testing Case 2
result = prod_or_sum(40, 30)
print("The result is", result)

# end of programme