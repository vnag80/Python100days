

fruits = ["Apple","Grape","kiwi"]
for index,fruit in enumerate(fruits):
    print(index)
    print(fruit)

nums = [1,1,1,2,2,2]
expectedNums = []
length = len(nums)
prev = 0
for i in range(0, length - 1):

    if nums[i] != nums[i + 1]:
        nums.remove()
        expectedNums.append(nums[i])
expectedNums.append(nums[length - 1])
print(expectedNums)