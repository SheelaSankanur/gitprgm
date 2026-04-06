def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst)-1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst

nums = [1, 2, 3, 4, 5]
print("Original list:", nums)
print("Reversed list:", reverse_list(nums))