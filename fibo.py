import math
import matplotlib.pyplot as plt
import numpy as np



#for i in range(3, 10):
#    print(i*i)


def fib(n):
    """Print Fibo Numbers"""

    result = []
    a, b = 0, 1
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fib2(n):
    a, b = 0, 1
    counter = 0
    while counter<n:
        a, b = b, a+b
        counter +=1
    return a

#print([fib(i) for i in range(20)])

phi0= (1+math.sqrt(5))/2
phi= [abs(fib2(i)/fib2(i-1)-phi0) for i in range(2,40)]
phi00 = [0 for i in range(2,40)]

print([(fib2(i)/fib2(i-1)-phi0) for i in range(2,40)]) # todo asd
#print((1+math.sqrt(5))/2)

# este mensaje lo grabe despues


plt.plot(range(2,40),phi00,label='phi0')
plt.plot(range(2,40),phi,'ro',label='fibo')
#plt.yscale('log')
plt.grid(True)
plt.legend()

plt.show()

#pi=3.14159
#x = np.linspace(0, 8*pi, 1000)
#f =np.sin(x)

#print(f)
#plt.plot(x,f)
#plt.show()
