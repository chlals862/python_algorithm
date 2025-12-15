resultList = []

for i in range(5):
    resultList.append(int(input()))

resultList.sort()

print(sum(resultList) // 5 , resultList[2])