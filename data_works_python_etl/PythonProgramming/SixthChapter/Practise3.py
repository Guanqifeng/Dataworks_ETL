# sphereArea(radius)返回具有给定半径的球体的表面积。
# sphereVolume(radius)返回具有给定半径的球体的体积。
# V = (4 / 3) * round(math.pi, 2) * r * r * r
# A = 4 * round(math.pi, 2) * r ** 2
import math

def sphereArea(radius):
    if radius:
        A = 4 * round(math.pi, 2) * radius ** 2
    else:
        A = ''
        print("Input Program is None! is :"+radius)
    return A
def sphereVolume(radius):
    if radius:
        V = (4 / 3) * round(math.pi, 2) * radius * radius * radius
    else:
        V = ''
        print("Input Program is None! is :"+radius)
    return V

if __name__ == '__main__':
    radius = 10
    print("Radius is :{0} And Area is :{1}".format(radius,sphereArea(radius)))
    print("Radius is :{0} And Volume is :{1}".format(radius,sphereVolume(radius)))