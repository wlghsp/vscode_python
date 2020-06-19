# 주어진 변수(num_10) 직접 수정불가
# 함수(prime_number) 직접 수정가능
num_10 = int(input("숫자를 입력해주세요: "))

def prime_number(n):
    if n != 1:
        for f in range(2, n):
            if n % f == 0:
                return False
    else:
        return False

    return True


if prime_number(num_10):
    print("소수")
else:
    print("소수가 아닙니다.")