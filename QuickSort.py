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

y = lambda a, b, c: a + b + c
print(y(43,98,12))




