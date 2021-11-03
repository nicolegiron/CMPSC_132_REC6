# Recitation Activity #6

def getLeftChild(aHeap, index):
    '''
        >>> getLeftChild([14, 9, 11, 5, 2, 10, 6], 1)
        9
        >>> getLeftChild([14, 9, 11, 5, 2, 10, 6], 2)
        5
        >>> getLeftChild([14, 9, 11, 5, 2, 10, 6], 6)
        >>> getLeftChild([14, 9, 11, 5, 2, 10, 6], 3)
        10
        >>> getLeftChild([56, 9, 15, 1, 2, 8], 3)
        8
        >>> getLeftChild([56, 9, 15, 1, 2, 8], 4)
    '''
    p = 2*index-1
    if index <= 0 or p >= len(aHeap):
        return None
    return aHeap[p]
