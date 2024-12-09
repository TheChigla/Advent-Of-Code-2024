safes = 0


def is_asc(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i] or abs(nums[i] - nums[i - 1]) not in [1, 2, 3]:
            return False

    return True


def is_desc(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i] or abs(nums[i] - nums[i - 1]) not in [1, 2, 3]:
            return False

    return True


with open('input.txt', 'r') as file:
    for line in file:
        nums = list(map(int, line.split(' ')))

        if is_asc(nums) or is_desc(nums):
            safes += 1

print(safes)
