# BOJ 1107
# 리모컨으로 채널 옮기기. 현재 채널은 100번
# 옮기고자 하는 채널, 고장난 버튼의 갯수, 고장난 숫자 버튼이 주어진다. 
# +, -버튼으로 채널 하나씩 이동 가능.
# 옮기고자 하는 채널에 가려면 최소 몇 번의 버튼을 눌러야 하는 지 출력한다. 
# 일단 고장나지 않은 버튼으로 최대한 비슷하게 만든 후에 +, -로 조정해야 되지 않을까?

N = int(input())
M = int(input())
wrong = list(map(int, input().split()))

diff_origin = abs(N - 100)

for num in range(1000001) : 
    num = str(num)
    
    for i in range(len(num)) : 
        if int(num[i]) in wrong : 
            break
        elif i == len(num) - 1 : 
            diff_origin = min(diff_origin, abs(int(num) - N) + len(num))

print(diff_origin)
