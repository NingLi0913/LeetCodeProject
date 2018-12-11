class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        result = []
        for i in range(len(nums)):
            if nums[i] in dict:
                result = [dict[nums[i]], i]
            dict[target - nums[i]] = i
        return result

if __name__ == '__main__':
    demo = Solution()
    Input1 = [1, 3, 5]
    Input2 = 6
    Output = demo.twoSum(Input1, Input2)
    print(Output)