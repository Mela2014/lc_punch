class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums: return 0
        bit_count, n, rslt = collections.defaultdict(int), len(nums), 0
        for num in nums:
            i = 0
            while num:
                if num & 1:
                    bit_count[i] += 1
                num >>= 1
                i += 1
        for _ , val in bit_count.items():
            rslt += val*(n-val)
        return rslt

    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums: return 0
        n, rslt =  len(nums), 0
        for bits in zip(*map("{:032b}".format, nums)):
            c = bits.count("1")
            rslt += c*(n-c)
        return rslt
