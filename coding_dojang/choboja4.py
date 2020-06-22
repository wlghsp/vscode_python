
# a = int(input("숫자를 입력하세요: "))

# print(a + 10)

# a = int(input("숫자를 입력하세요: "))

# if a % 2==0:
#     print("짝수")
# else:
#     print("홀수")

# a = int(input("숫자를 입력하세요: "))

# if a+20 <= 255:
#     print(a+20)
# else:
#     print(255)

# 115번
# a = int(input("숫자를 입력하세요: "))
# b = a - 20

# if b < 0:
#     print(0)
# elif b > 255:
#     print(255)
# else:
#     print(b)

# 116번
# a = input("현재 시간: ")

# if a[-2:]=="00":
#     print("정각입니다.")
# else: 
#     print("정각이 아닙니다.")

# 117번
# fruit = ["사과", "포도", "홍시"]
# user = input("좋아하는 과일은? ")
# if user in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 118번
# warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
# 종목 = input("원하는 종목은? ")

# if 종목 in warn_investment_list:
#     print("투자 경고 종목입니다.")
# else:
#     print("투자 경고 종목이 아닙니다.")

# 119번
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# 계절 = input("제가 좋아하는 계절은? ")

# if 계절 in fruit:
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 120번
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# 과일 = input("제가 좋아하는 과일은? ")

# if 과일 in fruit.values():
#     print("정답입니다.")
# else:
#     print("오답입니다.")

# 121번
# letter = input()

# if letter.islower():
#     print(letter.upper())
# else:
#     print(letter)

# 122번
# score = int(input("점수는? "))
# if score >= 81:
#     print("A")
# elif score >= 61:
#     print("B")
# elif score >= 41:
#     print("C")
# elif score >= 21:
#     print("D")
# else:
#     print("E")

# 123번
# 환율 = {"달러":1167, "엔":1.096,"유로":1268, "위안":171}
# user = input("입력: ")
# num, currency = user.split()
# print(float(num)* 환율[currency], "원")

# 124번
# number1 = int(input("input number1: "))
# number2 = int(input("input number2: "))
# number3 = int(input("input number3: "))

# if number1 > number2 and number1 > number3:
#     print(number1)
# elif number2 > number1 and number2 > number3:
#     print(number2)
# else:
#     print(number3)

#125번
# telnum = input("휴대전화 번호 입력: ")
# num = telnum.split("-")[0]
# if num == "011":
#     com ="SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# elif num == "010":
#     com = "알수없음"
# print(f"당신은 {com}사용자입니다.")

#126번  
# postcode = input("우편번호: ")

# if postcode[:3] in ["010","011","012"]:
#     print("강북구")
# elif postcode[:3] in ["013","014","015"]:
#     print("도봉구")
# else:
#     print("노원구")

#127번
# regNum = input("주민등록번호: ")
# num = regNum.split("-")[1]

# if num[0] == "1" or num[0] == "3":
#     print("남자")
# else:
#     print("여자")

#128번
# regNum = input("주민등록번호: ")
# num1 = regNum.split("-")[1]
# num = int(num1[1:3])

# if 0 <= num <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

#129번
# num = input("주민등록번호: ")
# first = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 + int(num[11]) * 4 + int(num[12]) * 5
# second = 11 - (first % 11)
# third = str(second)
# print(third)
# if num[-1] == third[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

#130번
