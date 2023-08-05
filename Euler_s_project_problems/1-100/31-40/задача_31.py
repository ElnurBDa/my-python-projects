c = [1, 2, 5, 10, 20, 50, 100]

max_c = [200, 100, 40, 20, 10, 4, 2]

ways = 0

sum = 0

from time import time
start=time()


for x6 in range(0, max_c[6] + 1):
    for x5 in range(0, max_c[5] + 1):
        for x4 in range(0, max_c[4] + 1):
            for x3 in range(0, max_c[3] + 1):
                for x2 in range(0, max_c[2] + 1):
                    for x1 in range(0, max_c[1] + 1):
                        for x0 in range(0, max_c[0] + 1):
                            sum += x0 * c[0] + x1 * c[1] + x2 * c[2] + x3 * c[3] + x4 * c[4] + x5 * c[5] + x6 * c[6]
                            if sum == 200:
                                ways += 1
                            sum = 0
print(ways + 1,time()-start)
input()
#73682 2409.088067293167
