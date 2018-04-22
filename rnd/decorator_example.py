from rnd import get_exec_time


@get_exec_time
def sqr(n):
    # time.sleep(1)
    return n*n


n = sqr(5)
print(n)
