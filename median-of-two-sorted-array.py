class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        size1 = len(nums1)
        size2 = len(nums2)
        merged = []
        n = 0 ; pointer1 = 0 ; pointer2 = 0
        while n < size1 + size2:

            if pointer1 == size1:
                merged = merged + nums2[pointer2::]
                break

            if pointer2 == size2:
                merged = merged + nums1[pointer1::]
                break

            if nums1[pointer1] <= nums2[pointer2]:
                merged.append(nums1[pointer1])
                pointer1 += 1

            else:
                merged.append(nums2[pointer2])
                pointer2 += 1
            n+= 1
        if len(merged) % 2 == 0:
            median1 = merged[len(merged)//2]
            median2 = merged[(len(merged)//2) - 1]
            median = (median1 + median2)/2.0
        else:
            median = merged[len(merged)//2]
        return median      




            