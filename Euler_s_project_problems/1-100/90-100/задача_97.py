def timer(func):
    def func_wrapper(*args, **kwargs):
        from time import time
        time_start = time()
        result = func(*args, **kwargs)
        time_end = time()
        time_spend = time_end - time_start
        print('%s cost time: %.3f s' % (func.__name__, time_spend))
        return result
    return func_wrapper


@timer
def mul(x):
    f=1
    for i in range(x):
        f*=2
        f=int(str(f)[::-1][:10][::-1])
    return f

@timer
def mul2(x):return str(2**x)[::-1][:9][::-1]


# a=[]
# for x in range(30, 10000):
#     y=str(2**x)[:10]
#     if y in a:break
#     a+=[y]

# print(len(a))





n=7830457
print(mul(n)*28433+1)
# 275808739992577