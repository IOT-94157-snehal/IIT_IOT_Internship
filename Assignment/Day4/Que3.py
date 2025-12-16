def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False



list1 = [3,4,5,7]
list2 = [8,6,2,1]

print(overlapping(list1, list2))