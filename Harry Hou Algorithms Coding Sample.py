"""
Harry Hou Algorithms Coding Sample
March 2023
Note that some of these searching and sorting algorithms look familiar 
to those in the Food Access Demographic Data project on GitHub:

https://github.com/HHou2/Food-Access-Demographic-Data/blob/main/backend.py

This code, however, has stripped unncessary information for clarity.
"""

def swap(lst, i, j):
    """
    Swaps the items in a function based on index.

    Parameters:
        lst: (lst) list of items
        i: (int) index of first item to swap
        j: (int) index of second item to swap
    Returns:
        none
    """

    tmp  = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp

def selection_sort(lst):
    """
    Uses a selection sorting algorithm to sort a list.

    Parameters:
        lst: (lst) list to sort
    Returns:
        sorted_lst: (lst) sorted list
    """

    for i in range(len(lst)):
        smallest_idx = i
        for j in range(i, len(lst)):
            if lst[j] < lst[smallest_idx]:
                smallest_idx = j
        swap(lst, i, smallest_idx)

    return lst

def lookbefore(lst):
    """
    Looks recursively for the same item as the last index.

    Parameters:
        lst: (lst) ordered list of items to search within
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    item = lst[len(lst)-1]
    idxs_found = []

    lst = lst[:len(lst)-1]

    look = True
    while look:
        if lst[:len(lst) - 1] == []:
            look = False
            return idxs_found
        elif lst[len(lst) - 1] == item:
            idxs_found.append(len(lst) - 1)
            lst = lst[:len(lst) - 1]
        elif lst[len(lst[:1]) - 1] != item:
            look = False
            return idxs_found

def lookafter(lst):
    """
    Looks recursively for the same item as the first index.

    Parameters:
        lst: (lst) ordered list of items to search within
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    item = lst[0]
    idxs_found = []

    lst = lst[1:]

    i = 1
    look = True
    while look:
        if lst[1:] == []:
            look = False
            return idxs_found
        elif lst[0] == item:
            idxs_found.append(i)
            lst = lst[1:]
            i += 1
        elif lst[0] != item:
            look = False
            return idxs_found

def binary_search(lst, item):
    """
    Uses a binary searching algorithm to find an item in an ordered list.

    Note: list must already be ordered beforehand.
    
    Parameters:
        lst: (lst) list to search within
        item: (str) item to search for
    Returns:
        idxs_found: (lst) list of indexes when item in lst
    """

    idxs_found = []

    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == lst[mid]:
            idxs_found.append(mid)

            # check indexes immediately before mid
            indexes_before_mid = lookbefore(lst[0:mid + 1])
            for i in range(len(indexes_before_mid)):
                idxs_found.append(indexes_before_mid[i])

            # corrects for Python counting from 0 error
            if (lst[0] == item) and (idxs_found[0] != 0):
                idxs_found.append(0)

            # check indexes immediately after mid
            indexes_after_mid = lookafter(lst[mid:])
            for i in range(len(indexes_after_mid)):
                idxs_found.append(mid + indexes_after_mid[i])

            return selection_sort(idxs_found)
        elif item < lst[mid]:
            high = mid - 1
        else:
            low = mid + 1

def main():
    """
    Main function for testing.

    Parameters:
        none
    Returns:
        none
    """

    # creating lists
    lst1 = ['cats', 'bears', 'parrots', 'fish', 'dogs', 'rhinos', 'dogs', \
            'goats', 'zebra']
    lst2 = [11, 72, 2, 13, 13, 42, 4, 6, 78]

    print("Here is lst1: %s" % lst1) # prints lst1
    print("Here is lst2: %s" % lst2) # prints lst2

    print()

    # sorting lists
    lst1_sorted = selection_sort(lst1) # prints lst1, but sorted
    lst2_sorted = selection_sort(lst2) # prints lst2, but sorted

    print("Here is lst1 sorted: " + str(lst1_sorted))
    print("here is lst2 sorted: " + str(lst2_sorted))

    print()

    # binary searching
    print("Index of 'dogs' in lst1, if it appears: %s" % \
          binary_search(lst1_sorted, 'dogs'))
    print("Index of 6 in lst2, if it appears: %s" % \
          binary_search(lst2_sorted, 6))

if __name__ == "__main__":
    main()