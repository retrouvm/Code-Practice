def solution(a):
    a_set=set()
    for i in a:
        if i in a_set:
            return i
        else:
            a_set.add(i)
    return -1