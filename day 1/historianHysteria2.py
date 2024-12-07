sum = 0
list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        nums = line.split('   ')

        list1.append(nums[0])
        list2.append(nums[1].replace('\n', ''))


for num in list1:
    sum += int(num) * list2.count(num)

print(sum)