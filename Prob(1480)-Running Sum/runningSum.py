def runningSum(nums):
        sumList = []
        sumList.append(nums[0])
        for i in range(1, len(nums)):
            sum = nums[i] + sumList[-1]
            sumList.append(sum)
        print(sumList)


if __name__ == '__main__':
    nums = []
    for i in range(int(input())):
        x = int(input())
        nums.append(x)
    runningSum(nums)