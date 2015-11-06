'''Returns factorial of n'''
n = 100
r = 1
for i in range(1, n + 1):
    r *= i

print(r,type(r))