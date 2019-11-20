sort = [10,3,7,9,15]
def BubbleSort():
    sort2 = sort
    for i in range(0, len(sort)):
        if sort[i] < sort[i+1]:
            sort[i], sort[i + 1] = sort[i + 1], sort[i]
    if( sort2 != sort):
        BubbleSort()
print(sort)


