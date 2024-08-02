#var2
"""
#변수 선언(변수명)
-숫자로 x
-공백 x
-특수문자 거의 x(_가능)
"""
season = "여름" 

print(season)

#실행이 안되는 에러를 "컴파일 에러"임-
#실행 후 나는 에러 "런타 에러"


#연습문제
name = 'Harin'
name = 'Jerry'
print(name)


print('*** 회원가입 ***')
user_id = 'jerry6'
user_pw = 'sf1234'
email = 'sldkfj@naver.com'
age = 12
print("아이디:",user_id)
print(f'아이디:{user_id}')
print("비밀번호:",user_pw)
print("email:",email)
print("나이:",age)


#8.1일
#소수점 처리
n1 = 10
n2 = 3
div = n1/n2
print(type(n1))
print(type(div))
print(f'결과값:{div:.2f}') #.f는 소수점 첫짜리, .2f는 소수점 둘째자
print(f'결과값:{round(div,2)})

#float:실수


#반올림 함수 -round(숫자, 자리수)
print(round(1.542,2))



