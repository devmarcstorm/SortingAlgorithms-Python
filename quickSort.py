def sort(uslist, le, ri):
    rip = ri
    lep = le
    pivot = uslist[le]
    while le < ri:
        if uslist[le+1] <= pivot:
            uslist[le], uslist[le+1] = uslist[le+1], uslist[le]
            le += 1
        else:
            if uslist[le+1] > pivot:
                uslist[le+1], uslist[ri] = uslist[ri], uslist[le+1]
                ri -= 1
    if le > lep + 1: sort(uslist, lep, le-1)
    if le < rip - 1: sort(uslist, le+1, rip)
    return uslist