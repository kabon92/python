# 1-100까지 랜덤숫자를 생성해서 정답을 맞추는 프로그램을 구현하시오.
# -----------------------
# 도전 회수 : 5
# 도전 번호 : [1,2,3,4,5]
# 랜덤 번호 : 5

# 1. 랜덤숫자 생성 
# 2. num list생성
# 3. n 변수 생성
# 4. 10번 for문생성
# 5. 입력한 숫자, num list에 저장
# 6. 정답비교
# 7. 데이터 출력

# import random

# lotto = []
# rnd_num = random.randint(1, 45)

# for i in range(6):
#     while rnd_num in lotto:
#         rnd_num = random.randint(1, 45)
#     lotto.append(rnd_num)

# lotto.sort()
# print("로또번호: {}".format(lotto))

import random

def number_guessing_game():
    random_number = random.randint(1, 100)  # 1~100 사이의 랜덤 숫자 생성
    attempts = []  # 사용자가 입력한 숫자 저장 리스트
    max_attempts = 10  # 최대 도전 횟수
    
    print("1부터 100 사이의 숫자를 맞혀보세요!")
    
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"{attempt}번째 시도: "))
            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력하세요.")
                continue
            
            attempts.append(guess)
            
            if guess == random_number:
                print(f"축하합니다! {attempt}번째 만에 정답을 맞추셨습니다!")
                break
            elif guess < random_number:
                print("더 큰 숫자를 입력하세요!")
            else:
                print("더 작은 숫자를 입력하세요!")
        
        except ValueError:
            print("숫자를 입력하세요.")
            continue
    else:
        print(f"아쉽습니다! 정답은 {random_number}였습니다.")
    
    print(f"도전 회수: {len(attempts)}")
    print(f"도전 번호: {attempts}")
    print(f"랜덤 번호: {random_number}")

if __name__ == "__main__":
    number_guessing_game()




