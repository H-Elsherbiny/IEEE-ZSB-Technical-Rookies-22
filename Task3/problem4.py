from sympy import symbols, solve

x = symbols('x')

lst = list(map(int, input().split()))

# =============================================================================
# Since they will reach the same position in the same time
# So the time is constant in the equation v = d / t
# d1 / v1 is equal to d2 / v2
# d = the new position - the initial position
# then we solve this equation to find the position 
# Since they move with just integers
# So if they will be at the same position so the x must be integer not flaot
# =============================================================================

eq = ((x - lst[0]) / lst[1]) - ((x - lst[2]) / lst[3])
sol = solve(eq)

y = float(sol[0])

if y == int(y):
    print("Yes")
    
else:
    print("No")    