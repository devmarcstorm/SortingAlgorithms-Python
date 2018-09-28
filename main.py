import bubbleSort
import insertionSort
import quickSort

#Unsorted list
clutter = [34, 19, 22, 51, 17, 5]
print "           " + "-".join(str(e) for e in clutter)

#Enable only one algorithm per run!

#print "bubble:    " + "-".join(str(e) for e in bubbleSort.sort(clutter))
#print "insertion: " + "-".join(str(e) for e in insertionSort.sort(clutter))
print "quickSort: " + "-".join(str(e) for e in quickSort.sort(clutter, 0, len(clutter)-1))