
test_list = [4, 5, 8, 9, 10, 17]
print("The original list : " + str(test_list))
test_list.sort()
mid = len(test_list) // 2
res = (test_list[mid] + test_list[~mid]) / 2
print("Median of list is : " + str(res))