from time import time

start = time()
a = 0
for x0 in range(0, 10):
    for x1 in range(0, 10):
        for x2 in range(0, 10):
            for x3 in range(0, 10):
                for x4 in range(0, 10):
                    for x5 in range(0, 10):
                        for x6 in range(0, 10):
                            for x7 in range(0, 10):
                                for x8 in range(0, 10):
                                    for x9 in range(0, 10):
                                        if x0 != x1 and x0 != x2 and x0 != x3 and x0 != x4 and x0 != x5 and x0 != x6 and x0 != x7 and x0 != x8 and x0 != x9 and x1 != x2 and x1 != x3 and x1 != x4 and x1 != x5 and x1 != x6 and x1 != x7 and x1 != x8 and x1 != x9 and x2 != x3 and x2 != x4 and x2 != x5 and x2 != x6 and x2 != x7 and x2 != x8 and x2 != x9 and x3 != x4 and x3 != x5 and x3 != x6 and x3 != x7 and x3 != x8 and x3 != x9 and x4 != x5 and x4 != x6 and x4 != x7 and x4 != x8 and x4 != x9 and x5 != x6 and x5 != x7 and x5 != x8 and x5 != x9 and x6 != x7 and x6 != x8 and x6 != x9 and x7 != x8 and x7 != x9 and x8 != x9:
                                            a += 1
                                            if a == 1000000:
                                                f=open('progress_задачв_24.txt','w+')
                                                print(time() - start)
                                                print(a, '|', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)
                                                f.write(str(a)+'|'+str(x0)+str(x1)+str(x2)+str(x3)+str(x4)+str(x5)+str(x6)+str(x7)+str(x8)+str(x9)+'\n'+str(time()-start)+'sec')
                                                f.close()
                                                
'''2783915460'''