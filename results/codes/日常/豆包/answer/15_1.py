def subsets(nums):
    result = [[]]
    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        result.extend(new_subsets)
    return result


nums = input("请输入一个数组，元素用逗号分隔：").split(',')
nums = [int(num) for num in nums]
print(subsets(nums))
    