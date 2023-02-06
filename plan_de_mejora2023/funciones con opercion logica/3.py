def xnor_operation(a, b):
    return not ((a and not b) or (not a and b))

print(xnor_operation(5,6))