#if문
#구문 만들때 끝에 클론(:)을 붙이고 다음줄에서 4칸 띄어씀(indent)
age = 17
'''
if age >= 15:  #조건이 True일때 실행
    print("관람가")
print(f"나이는 {age}세 입니다")#if문이 실행이 되지 않았을 때 출력
'''
#if ~else: 조건이 True 이면 if문, false이면 else문
if age >= 15:  #조건이 True일때 실행
    print("관람가")
if age < 15:
    print("관람불가")
print(f"나이는 {age}세 입니다")  #코드 실행이 끝났을 때

#어떤 수를 짝수인지 홀수인지 판별하는 프로그램
#짝수정의방법: 2로 나눈 나머지가 0
num = int(input("숫자를 입력하세요: "))
if num %2 ==0:
    print("짝수")
else:
    print("홀수")
print(f"입력된 수는 {num}입니다.")

#if조건1:
#    실행문
#elif조건2:
#    실행문
#else:
#    실행문
age = 25
if age < 20:
    print("미성년자")
elif age < 30:
    print("20대 입니다")
elif age < 40:
    print("30대 입니다")
else:
    print("이제는 중년..")
print(f'skdl')