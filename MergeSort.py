sort = [10,3,7,13,8]
def Merge(sort, f, m, l):
    x = m - f + 1
    y = l - m
    left = [None] * (x)
    right = [None] * (y)

    for i in range(0, x):
        left[i] = sort[f+i]
        i = i+1

    for j in range(0, y):
        right[j] = sort[m+1+j]
        j = j+1
    i, j, k = 0, 0, f
    while i < x and j < y:
        if left[i] <= right[j]:
            sort[k] = left[i]
            i = i+1
        else:
            sort[k] = right[j]
            j = j+1
        k = k+1



    while i < x:
        sort[k] = left[i]
        i = i + 1
        k = k + 1
    while j < y:
        sort[k] = right[j]
        j = j + 1
        k = k + 1


def MergeSort(sort, f, l):
    if f < l:
        m = int((l+f)/2)
        MergeSort(sort, f, m)
        MergeSort(sort, m+1, l)
        Merge(sort, f, m, l)
MergeSort(sort, 0, len(sort)-1)
print(sort)
