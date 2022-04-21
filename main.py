import numpy as np


def main():
    arr1 = np.transpose([1, 5, -3, 2])
    arr2 = np.transpose([8, 2, 4, 7])
    result = np.dot(arr1, arr2)


if __name__ == '__main__':
    main()
