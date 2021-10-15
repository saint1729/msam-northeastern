from multiprocessing import Pool
import time

def f(x):
    return x**2 + 2*x + 1

if __name__ == "__main__":
    n = 1000000
    pool = Pool()

    start = time.time()

    l = list(map(f, range(n)))
    # print(l)

    end1 = time.time()
    print(f"{end1 - start} seconds")

    l = pool.map(f, range(n))
    # print(l)

    end2 = time.time()
    print(f"{end2 - end1} seconds")

    l = []
    for i in range(n):
        l.append(i**2 + 2*i + 1)

    end3 = time.time()
    print(f"{end3 - end2} seconds")
