#포인트 : 변수에 숫자형 문자형 데이터를 담아 실행해보기 !
#자료형(type) - 숫자(정수, 실수), 문자
floor = 3 #정수 3을 저장하는 floor라는 변수
name = '김기용' # = 은 개인 연산자라 함
weight = 2.5
print(floor,"층")

#print("나는", floor, "층에 살아요", sep='')
#콤마는 뛰어쓰기, sep는 뛰어쓰기 초기화 여부

print(f'나는 {floor}층에 살아요')
print("내 이름은 " + name + "입니다") #연결 연산자라함 
#print("이 노트북의 무게는" + weight + "kg입니다") #str과 str은 문자만 연결, int형을 쓰고싶으면 문자형으로 변경필요
#str(숫자)쓰면 됨
print("내 몸무게는 " + str(weight) + "입니다")
print(f"나는 {weight}kg 입니다")
#type()--자료형을 인식하는 함수, 괄호 안에는 매개변수가 들어
print(type(floor))#integer 정수
print(type(weight))#float는 실수(부동)
print(type(name))#string은 문자






