import numpy as np


def main():

    a = np.array([1,2,5])
    b = np.array([[1,2,4], [4,5,6]])
    print(a)
    print(b)
    # 具体打印出来的看打印函数的实现，
    # 在 opencv 中对应的是高，宽，通道数
    c = np.zeros((8,8,3), np.uint8)
    print(c)
    # 全部填充 1
    d = np.ones((8,8), np.uint8)
    print(d)

    #  自定义填充的数据
    e = np.full((8,8), 255, np.uint8)
    print(e)

    f = np.identity(8)
    print(f)

    # 设置行列数
    # g = np.eye(6, 9)
    # 可以指定偏移量
    g = np.eye(6, 9, k=2)

    print(g)


if __name__ == "__main__":
    main()
