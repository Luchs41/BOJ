# BOJ 9461
# 파도반 수열을 출력한다. 
# 초기에 변의 길이가 1인 정삼각형이 있다. 이 후 나선에서 가장 긴  변의 길이를 k라고 했을 때, 길이가 k인 정삼각형을 추가한다. 
# 미리 100번째 값까지 구해놓고 입력값에 따라 출력한다. 
from collections import deque
caseN = int(input())
arr = deque()
arr.append(1)
arr.append(1)
arr.append(1)
arr.append(2)
arr.append(2)
for i in range(5, 101) : 
    arr.append(arr[i - 1] + arr[i - 5])

for _ in range(caseN) : 
    N = int(input())
    print(arr[N - 1])
