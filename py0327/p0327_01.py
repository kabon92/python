# 파이썬 변수타입
# - bool타입 - Ture,false 
# 숫자 : int타입-정수,float타입-실수 
# str타입 
 
# #print()
# print("안녕")

# # 변수선언
# 변수 = 10
# a = 20
# num = 30

# print("안녕")
# print("입력된 숫자 :",a)
# print("입력된 숫자 : %d" % (a))
# print("입력된 숫자 : {}" .format(a))
# print(f"입력된 숫자 : {a}")

# 입력 - input => 타입 : str타입 문자열타입
# 입력된 값은 타입 : str타입이기 때문에 형변환을 해줘야함.
# num1 = int(input("숫자를 입력하세요.>> ")) # 문자열 
# num2 = int(input("숫자를 입력하세요.>> ")) # 문자 숫자 변경해야됨 
# print("입력된 숫자 : {},{} / 합계 : {}".format(num1,num2,num1+num2))


# 학생성적 프로그램
# 이름,국어,영어,수학 입력받아, 합계,평균을 출력하는 프로그램을 구현
print("-"*50)
print("                학생성적프로그램")
print("-"*50)
name = input("이름을 입력하세요.") #str타입
kor = int(input("국어점수를 입력하세요.>> "))
eng = int(input("영어어점수를 입력하세요.>> "))
math = int(input("수학점수를 입력하세요.>> "))
total = kor+eng+math
avg = (kor+eng+math)/3
print()
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("{}\t{}\t{}\t{}\t{}\t{:.2f}".format(name,kor,eng,math,kor+eng+math,avg)) # 갯수를 맞춰야 합니다.


