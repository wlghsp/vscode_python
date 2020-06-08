# -*- coding: utf-8 -*- 
# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n 
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

def sum(n):
    if n == 0:
       return 0
    return sum(n - 1)+ n 

print(sum(10))
print(sum(100))
