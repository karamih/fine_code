class FindingPair:
    def __init__(self, nums: list, target: int):
        self.nums = nums
        self.target = target

    def approach_one(self):
        for num in self.nums:
            complement = self.target - num
            if complement in self.nums and complement != num:
                return num, complement
        return None

    def approach_two(self):
        seen = {}
        for num in self.nums:
            complement = self.target - num
            if complement in seen:
                return num, complement
            seen[num] = True
        return None

    def approach_three(self):
        # self.nums.sort()
        nums = sorted(self.nums)
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == self.target:
                return nums[left], nums[right]
            elif current_sum < self.target:
                left += 1
            else:
                right -= 1

        return None


numbers = [2, 5, 3, 8, 6, 11]
target = 8
finder = FindingPair(nums=numbers, target=target)

print(f'Approach One => pair with {target} as summation is: {finder.approach_one()}')
print(f'Approach Two => pair with {target} as summation is: {finder.approach_two()}')
print(f'Approach Three => pair with {target} as summation is: {finder.approach_three()}')

# Approach One => pair with 8 as summation is: (2, 6)
# Approach Two => pair with 8 as summation is: (3, 5)
# Approach Three => pair with 8 as summation is: (2, 6)
