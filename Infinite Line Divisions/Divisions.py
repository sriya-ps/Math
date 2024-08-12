import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt	

a=1
b=2
m=3
n=1
kmax=10

def x(k, memo={}):
    if k in memo:
        return memo[k]
    if k == 0:
        return a
    elif k == 1:
        return b
    memo[k] = ((m*x(k-1) + n*x(k-2))/(m+n))
    return memo[k]

xseq = np.array([x(i) for i in range(kmax)])
kseq = np.array([i for i in range(kmax)])
print("( k , x(k) )")
for i in range(kmax):
    print("(",kseq[i], ",", xseq[i],")")
xinf_num=(m+n)*b+n*a
xinf_den=(m+n)+n
xinf = xinf_num/xinf_den

interpolation = interp1d(kseq, xseq, kind = "quadratic")
k_=np.linspace(kseq.min(), kseq.max(), 500)
x_=interpolation(k_)

plt.title('Infinite Line Divisions')
plt.xlabel('k')
plt.ylabel('x(k)')
plt.scatter(kseq, xseq)
plt.plot(k_, x_)
plt.plot([0, kmax], [xinf, xinf], linestyle='dashed')
plt.text(kmax-0.5,xinf+0.02,str(xinf_num)+"/"+str(xinf_den))
plt.show()