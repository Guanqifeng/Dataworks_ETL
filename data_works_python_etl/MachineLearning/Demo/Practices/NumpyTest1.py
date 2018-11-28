import matplotlib.pyplot as plt
import numpy as np
def plot_test():
    point = np.arange(-5,5,0.01)
    xs , ys = np.meshgrid(point,point)
    z = np.sqrt(xs ** 2 + ys ** 2)
    plt.title("Image plot of $\sqrt(x^2 + y^2)$ for a grid of values")
    plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()

if __name__ == '__main__':
    plot_test()