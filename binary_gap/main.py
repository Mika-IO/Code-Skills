def solution(N):
    if (type(N) == int) and (N > 0):
        n  = bin(N)[2:]
        gaps = n.split('1')
        del(gaps[0])
        del(gaps[len(gaps)-1])
        if len(gaps) > 0:
            max_gap = max([len(g) for g in gaps])
            return max_gap
        else:
            return 0
    else:
        return 0
