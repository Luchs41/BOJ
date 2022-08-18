# BOJ 2609
# 최대공약수와 최소공배수
# 두 수의 최대공약수와 최소공배수를 출력한다. 
a, b = map(int, input().split())

import math

print(math.gcd(a, b))
print(math.lcm(a, b))