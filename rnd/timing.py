def get_exec_time(myfunc):
    from datetime import datetime

    def run_func(*args, **kwargs):
        t1 = datetime.now()

        ret_val = myfunc(*args, **kwargs)
        t2 = datetime.now()
        print("elapsed time:", t2-t1)
        return ret_val
    return run_func
