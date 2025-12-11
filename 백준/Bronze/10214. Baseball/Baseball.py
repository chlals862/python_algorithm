T = int(input())

for i in range(T):
    A,B = 0, 0
    for j in range(9):
        Y,K = map(int, input().split())
        A += Y
        B += K
  
    if A == B:
      print("Draw")
    elif A > B:
      print("Yonsei")
    elif A < B:
      print("Korea")