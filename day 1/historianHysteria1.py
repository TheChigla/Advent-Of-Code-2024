sum = 0
list1, list2 = [], []

with open("input.txt", "r") as file:
    for line in file:
        nums = line.split('   ')

        list1.append(nums[0])
        list2.append(nums[1].replace('\n', ''))


list1, list2 = sorted(list1), sorted(list2)

for i in range(len(list1)):
    sum += abs(int(list1[i]) - int(list2[i]))

print(sum)


