sort_list = [10,7,5,8,20,1,0]
def Partition(sort_list, p, r):
    for x in range(p,r):
        if  sort_list[x] < sort_list[r]:
            sort_list[p], sort_list[x] = sort_list[x], sort_list[p]
            p = p+1
    sort_list[p], sort_list[r] = sort_list[r], sort_list[p]
    return p
def Quick_sort(sort_list, p, r):
    if p < r:
        x = Partition(sort_list, p, r)
        Quick_sort(sort_list, p, x-1)
        Quick_sort(sort_list, x + 1, r)
Quick_sort(sort_list, 0, len(sort_list)-1)
print(sort_list)

def Quick(sort_list, n, f, l):
    m = int((f+l)/2)
    if sort_list[m] == n :
        print("Element found at index "+str(m))
    elif sort_list[m] < n and m < l:
        Quick(sort_list, n, m+1, l)
    elif sort_list[m] > n and m > f:
        Quick(sort_list, n, f, m)
    else:
        print("Element not found at inder")
Quick(sort_list, 5, 0, len(sort_list)-1)








