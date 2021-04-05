import time

n = 0

def progressbar(lst):
    global n
    len_ = len(lst)
    if n > len_:
        return -1
    st = "=" * int(n/10)
    if st == "":
        st += '-'
    else:
        st += ">"
    tmp = round(time.process_time() * 10, 3)
    t = round((n * 10/len_), 3)
    print("ETA: {time} [{percent}%] [{str:<100}] {n}/{lenght} | elapsed time {times}s".format(
        time=t, percent=n/10, str=st, n=n, lenght=len_, times=tmp), end="\r")
    n += 1
    yield n
