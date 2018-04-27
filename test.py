import matplotlib.pyplot as plt

def logWachstumEuler(r, h, K, N0, Tend):
    N=[N0]
    for k in range(0,Tend):
        t=k*h
        N.append(N[-1]+h*f(N[-1], r, K, t))
    return N

def logWachstumHeun(r, h, K, N0, Tend):
    N=[N0]
    for k in range(0,Tend):
        t=k*h
        N_P = N[-1]+h*f(N[-1], r, K, t)
        N.append(0.5*N[-1] + 0.5*(N_P + h*f(N_P, r, K, (k+1)*h)))
    return N

def f(Nt, r, K, t):
    return r*Nt*(1-Nt/K)

print("Hello there, fellow ghost!")
plt.ylabel('N')
plt.xlabel('t')
plt.subplot(211)
plt.plot(logWachstumEuler(20, 0.01, 100, 5, 100))
plt.plot(logWachstumEuler(20, 0.01, 100, 20, 100))
plt.plot(logWachstumEuler(20, 0.01, 200, 5., 100))
plt.plot(logWachstumEuler(20, 0.1, 100, 5., 100))
plt.subplot(212)
plt.plot(logWachstumHeun(20, 0.01, 100, 5, 100))
plt.plot(logWachstumHeun(20, 0.01, 100, 20, 100))
plt.plot(logWachstumHeun(20, 0.01, 200, 5., 100))
plt.plot(logWachstumHeun(20, 0.1, 100, 5., 100))
plt.show()