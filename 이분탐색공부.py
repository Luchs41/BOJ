# buckets에서 m개의 수를 골라
# 각 수의 차이의 최소값이 최대값을 출력
# ex) 1, 4, 7 -> answer = 3
# 최대 10000개 숫자 / 위치 ~ 1000000
def solution(buckets, m):
    def can_place(buckets, m, Min) : 
        count = 1
        last = buckets[0]
        for num in buckets : 
            if num - last >= Min : 
                count += 1
                last = num
        return count >= m
    buckets.sort()
    
    left = 0
    right = buckets[-1] - buckets[0]
    answer = 0
    selected_numbers = []

    while left <= right : 
        mid = (left + right) // 2

        if can_place(buckets, m, mid) : 
            answer = mid
            selected_numbers = []
            last_position = buckets[0]

            for num in buckets : 
                if num - last_position >= mid : 
                    selected_numbers.append(num)
                    last_position = num
            left = mid + 1
        else : 
            right = mid - 1
    
    
    

    return answer

buckets = [1, 2, 3, 4, 9]
m = 3
print(solution(buckets, m))
'''
6, 3, 2, 1
5, 2, 1
4, 3
3
'''