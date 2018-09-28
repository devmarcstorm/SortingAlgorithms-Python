def sort(uslist):
    size = len(uslist)
    for i in range(1, size):
        j = i
        obj = uslist[i]
        while j > 0 and uslist[j-1] > obj:
            obj1 = uslist[j]
            obj2 = uslist[j-1]
            uslist[j] = obj2
            uslist[j-1] = obj1
            j -= 1
        uslist[j] = obj
    return uslist