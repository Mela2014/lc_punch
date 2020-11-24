class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2: return [-1]*len(nums1)
        keeper, stk = {}, [nums2[0]]
        for num in nums2[1:]:
            while stk and num > stk[-1]:
                temp = stk.pop()
                keeper[temp] = num
            stk.append(num)
        rslt = []
        for num in nums1:
            rslt.append(keeper.get(num, -1))
        return rslt
            
