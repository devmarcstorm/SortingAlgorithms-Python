def sort(uslist):
    size = len(uslist)
    while size > 1:
        for i in range(0, size - 1):
            obj1 = uslist[i]
            obj2 = uslist[i+1]
            if obj1 > obj2:
                uslist[i] = obj2
                uslist[i+1] = obj1
        size -= 1
    return uslist