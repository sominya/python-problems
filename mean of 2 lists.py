nums1 = [0,0]
nums2 = [1,2]

def meanoftwolists(l1,l2):
    lst = l1+l2
    lst.sort()
    len_lst = len(lst)
    if len_lst == 1:
        mean = lst[0]
    elif len_lst%2 == 0 and len_lst != 1:
        mean = (lst[int(len_lst/2)]+lst[(int(len_lst/2)-1)])/2
    else:
        mean = lst[int(len_lst/2)]
    return mean
