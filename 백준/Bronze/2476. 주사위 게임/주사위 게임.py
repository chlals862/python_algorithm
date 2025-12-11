N = int(input())
result = []

for i in range(N):
  A,B,C = map(int, input().split())

  if A == B == C:
    prize = 10000 + A * 1000
  elif A == B or A == C:
    prize = 1000 + A * 100
  elif B == C:
    prize = 1000 + B * 100
  elif A != B != C:
    prize = max(A,B,C) * 100

  result.append(prize)
print(max(result))