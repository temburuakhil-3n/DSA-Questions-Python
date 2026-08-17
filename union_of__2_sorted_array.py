nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8] 

nums1.extend(nums2)
nums1=list(set(nums1))
nums1.sort()
print(nums1)