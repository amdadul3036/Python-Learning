x = 2**3
# It represents 2^3 
print(x)

# -------------------------------------------------------------------------------------------

def exponential(base , power):
    result = 1
    for i in range(power):
        result = result*base
    return result

final = exponential(2,7)
print(final)