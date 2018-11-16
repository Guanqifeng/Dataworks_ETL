from numpy import *
import pylab

def numpyTest1():
    a = arange(15).reshape(3,5)
    b = array([6, 7, 8])
    c = array([2.1,4.3,6.5])
    #d = array(2.1,4.3,6.5) #wrong
    d = array([[1,2,3],[4,5,6]])
    e = zeros((3,4))
    print(a)
    print(a.shape)
    print(a.ndim)
    print(a.dtype.name)
    print(a.size)
    print(type(a))
    print(b)
    print(b.ndim)
    print(type(b))
    print(a.itemsize)
    print(c.dtype)
    print(d)
    print(e)
def numpyTest2():
    A = arange(12)
    A.shape = (3,4)
    M = mat(A.copy())
    print(str(type(A))+" "+str(type(M)))
    print(M)
    print(A[:, 2])
    print(A[:,[1,3]])
    print(A[:,A[0,:]>1])
def numpyTest3():
    # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
    mu, sigma = 2, 0.5
    v = random.normal(mu, sigma, 10000)
    # Plot a normalized histogram with 50 bins
    pylab.hist(v, bins=50, normed=1)  # matplotlib version (plot)
    pylab.show()
    # Compute the histogram with numpy and then plot it
    (n, bins) = histogram(v, bins=50, normed=True)  # NumPy version (no plot)
    pylab.plot(.5 * (bins[1:] + bins[:-1]), n)
    pylab.show()
if __name__ == '__main__':
    #numpyTest1()
    #numpyTest2()
    numpyTest3()