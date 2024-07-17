import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def partFive():
    first = np.random.multivariate_normal([1, 1], [[1, 0], [0, 1]], 10)
    second = np.random.multivariate_normal([1, 2], [[1, 0], [0, 1]], 10)
    third = np.random.multivariate_normal([2, 1], [[1, 0], [0, 1]], 10)

    for i in range(len(first)):
        plt.plot(first[i, 0], first[i, 1], 'ro')
        plt.text(first[i, 0], first[i, 1], '0')

    for i in range(len(second)):
        plt.plot(second[i, 0], second[i, 1], 'bo')
        plt.text(second[i, 0], second[i, 1], '1')

    for i in range(len(third)):
        plt.plot(third[i, 0], third[i, 1], 'yo')
        plt.text(third[i, 0], third[i, 1], '2')

    plt.ioff()
    plt.show()


def partFour():
    x = np.random.uniform(0, 1, 20)
    n = np.random.normal(0, 0.3, 20)

    y = np.sin(2 * np.pi * x) + n
    plt.title("Krenar Banushi Part 4 Plot")
    plt.plot(x, y, 'ro')
    plt.show()


a = np.array([[1, 2, 3], [0, 1, 3], [1, 0, 8]])
b = np.array([[7, 9, 2], [3, 4, 3], [6, 1, 3]])

print("Element wise multiplication:\n", a * b)
print()
c = a.__imatmul__(b)

print("Matrix multiplication:\n", c)
print()

aInverse = la.inv(a)
aT = a.transpose()
aTa = a.dot(aT)

print("Inverse:\n", aInverse)
print()
print("Transpose:\n", aT)
print()
print("A * A Transpose:\n", aTa)
print()

a = np.array([1, -1, 0])
b = np.array([0, 1, 1])

aNormOne = la.norm(a, 1)
aNormTwo = la.norm(a, 2)
bNormOne = la.norm(b, 1)
bNormTwo = la.norm(b, 2)
abNormOne = la.norm(a - b, 1)
abNormTwo = la.norm(a - b, 2)

print("Norm One of A:\n", aNormOne)
print("Norm Two of A:\n", aNormTwo)
print("Norm One of B:\n", bNormOne)
print("Norm Two of B:\n", bNormTwo)
print("Norm One of A - B:\n", abNormOne)
print("Norm Two of A - B:\n", abNormTwo)

selection = input("Enter 1 for part4 plot, else for part5:")
if selection == "1":
    partFour()
else:
    partFive()
