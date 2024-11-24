class FindingPair:
    """
    A class to find pairs of numbers that sum up to a given target.

    Attributes:
        nums (list): A list of integers to search for pairs.
        target (int): The target sum for which pairs will be found.

    Methods:
        approach_one: Finds a pair of numbers from `nums` that sum to the target using a brute-force method.
        approach_two: Finds a pair using a hash set for faster lookup.
        approach_three: Finds a pair by sorting the list and using a two-pointer technique.
    """

    def __init__(self, nums: list, target: int):
        """
        Initializes the FindingPair object with a list of numbers and a target sum.

        Args:
            nums (list): A list of integers to search for pairs.
            target (int): The target sum to find pairs for.
        """
        self.nums = nums
        self.target = target

    def approach_one(self):
        """
        Finds a pair of numbers from `nums` that sum up to the target using a brute-force method.

        Iterates over the list and checks if the complement (target - current number) exists in the list.
        This approach has a time complexity of O(n^2) due to nested iteration.

        Returns:
            tuple: A tuple containing a pair of numbers that sum to the target, or None if no such pair exists.
        """
        for num in self.nums:
            complement = self.target - num
            if complement in self.nums and complement != num:
                return num, complement
        return None

    def approach_two(self):
        """
        Finds a pair of numbers from `nums` that sum up to the target using a hash set for faster lookup.

        This approach reduces the time complexity to O(n) by using a dictionary to store seen numbers.

        Returns:
            tuple: A tuple containing a pair of numbers that sum to the target, or None if no such pair exists.
        """
        seen = {}
        for num in self.nums:
            complement = self.target - num
            if complement in seen:
                return num, complement
            seen[num] = True
        return None

    def approach_three(self):
        """
        Finds a pair of numbers from `nums` that sum up to the target using a two-pointer technique after sorting the list.

        This approach has a time complexity of O(n log n) due to sorting, followed by a linear scan.

        Returns:
            tuple: A tuple containing a pair of numbers that sum to the target, or None if no such pair exists.
        """
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


# Example usage
numbers = [2, 5, 3, 8, 6, 11]
target = 8
finder = FindingPair(nums=numbers, target=target)

print(f'Approach One => pair with {target} as summation is: {finder.approach_one()}')
print(f'Approach Two => pair with {target} as summation is: {finder.approach_two()}')
print(f'Approach Three => pair with {target} as summation is: {finder.approach_three()}')
