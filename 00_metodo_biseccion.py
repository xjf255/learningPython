formula = "-2+7*x-5*x**2+6*x**3"
interval = [0, 1]
tolerance = 0.001

def evaluate_formula(x_value):
    """Safely evaluate the formula for a given x value"""
    # Using eval but with a safer approach by defining the variable explicitly
    x = x_value
    return eval(formula)

def resolve(interval, iteration = 1):
    first_value = interval[0]
    second_value = interval[1]
    current_value = (first_value + second_value) / 2
    
    fn_first = evaluate_formula(first_value)
    fn_second = evaluate_formula(second_value)
    fn_current = evaluate_formula(current_value)
    
    error = abs((second_value - first_value) / 2)
    
    print(f"Interation # {iteration}")
    print(f"Interval: [{first_value:.6f}, {second_value:.6f}]")
    print(f"Current value: {current_value:.6f}")
    print(f"Function at current value: {fn_current:.6f}")
    print(f"Error: {error:.6f}")
    
    # Check if we've reached the desired tolerance
    if error <= tolerance:
        return current_value
    
    # Check which subinterval contains the root
    if fn_first * fn_current < 0:  # Root is in [first_value, current_value]
        return resolve([first_value, current_value],iteration+ 1)
    elif fn_current * fn_second < 0:  # Root is in [current_value, second_value]
        return resolve([current_value, second_value],iteration+ 1)
    else:
        # This can happen if we hit the root exactly or if there's no sign change
        if abs(fn_current) < tolerance:
            return current_value
        else:
            print("Warning: No sign change detected in interval. Method may not converge.")
            # Continue with the interval that has the smaller function value
            if abs(fn_first) < abs(fn_second):
                return resolve([first_value, current_value],iteration+ 1)
            else:
                return resolve([current_value, second_value],iteration+ 1)

# Call the function with the given interval
root = resolve(interval=interval)
print(f"\nApproximate root: {root:.6f}")
print(f"Function value at root: {evaluate_formula(root):.10f}")