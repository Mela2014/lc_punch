class SparseVector:
    def __init__(self, nums: List[int]):
        self.vec = {i:v for i, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        rslt = 0
        for i,v in self.vec.items():
            if i in vec.vec:
                rslt += v*vec.vec[i]
        return rslt
