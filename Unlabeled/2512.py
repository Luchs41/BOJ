# BOJ 2512
# 예산
# 1. 모든 요청이 배정 가능하면, 그대로 배정
# 2. 불가능하면 특정한 상한액 설정, 상한액 이상의 금액은 모두 상한액 배정
# 배정된 예산 중 최댓값 출력
# 이분탐색으로 fit한 값 찾기

N = int(input())
budget = list(map(int, input().split()))
maximum = int(input())
start = 0
end = max(budget)
while start <= end:
  mid = (start + end) // 2
  result = 0
  for b in budget:
    if b > mid:
      result += mid
    else:
      result += b
  if result <= maximum:
    start = mid + 1
  else:
    end = mid - 1
print(end)