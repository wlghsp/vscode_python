# 리스트에서 특정 숫자 위치 전부 찾기
# 입력: 리스트 a, 찾는 값 x 
# 출력: 찾는 값의 위치 번호가 담긴 리스트, 찾는 값이 없으면 빈 리스트 []

def search_list(a,x):
    n = len(a)          # 입력 크기 n 
    result = []         # 새 리스트를 만들어 결괏값을 저장
    for i in range(0,n): # 리스트 a의 모든 값을 차례로
        if x == a[i]:   # x 값과 비교하여 
           result.append(i)    
        
    return result    # 만들어진 결과 리스트를 돌려줌     

v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 18)) # 2 (순서상 세번째지만 위치번호는 2)
print(search_list(v, 33)) # 3 ( 33은 리스트에 두 번 나오지만 처음 나온 위치만 출력)
print(search_list(v, 900)) # -1(900은 리스트에 없음 )