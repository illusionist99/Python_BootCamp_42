import time
import sys

n = 0


def ft_progress(lst):
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

listy = range(1000)
ret = 0


while range(len(listy)):
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        time.sleep(0.001)
    if elem == -1:
        break
    #print()
    #print(ret)