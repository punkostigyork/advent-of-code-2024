list1 = []
list2 = []

with open('input.txt', 'r') as f:
    for line in f:
        num1, num2 = map(int, line.split('   '))
        list1.append(num1)
        list2.append(num2)

sum = 0
for i in range(len(list1)):
    sum = sum + list1[i] * list2.count(list1[i])

print(sum)