a=1
b=2
m=1
n=1
kmax=20

def x(k, memo={}):
    if k in memo:
        return memo[k]
    if k == 0:
        return a
    elif k == 1:
        return b
    memo[k] = ((m*x(k-1) + n*x(k-2))/(m+n))
    return memo[k]

xseq = [x(i) for i in range(kmax + 1)]
print(xseq)