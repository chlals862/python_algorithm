N = int(input())
resultList = list(map(int, input().split()))

resultList.sort()

print(resultList[0], resultList[-1])