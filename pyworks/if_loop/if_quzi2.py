# score = int(input("점수를 입력하세요:"))
#
# if score >= 90:
#     print("A등급입니다")
# elif score >=80 and score < 90:
#     print("B등급입니다")
# elif score >=70 and score < 80:
#     print("C등급입니다")
# elif score >=60 and score < 70:
#     print("D등급입니다")
# else:
#     print("E등급입니다")


#또 다른 방법
# score = int(input("점수를 입력: "))
# rank = ''
# if(score<0 or score>100):
#     rank = '잘못된 점수(입력 오류)'
# elif(score>= 90 and score <= 100):
#     rank = 'A'
# elif(score >= 80 and score <90):
#     rank = 'B'
# elif(score >= 70 and score <80):
#     ranke = 'C'
# elif(score>=60 and score < 70):
#     rank = 'D'
# else:
#     rank = 'E'
# print(f'{rank}등급입니다.')


#연령대로 나누고, 연령이 20대인 경우에만, 성별이 여이면, "20대 여성입니다" 출력하고,
#남이면, "20대 남성입니다" 출력.
age = int(input("연령을 입력하세요:"))
gender = "" #남/여
if age >= 0 and age <20:
    print("미성년자입니다")
elif age >= 20 and age <30:
    print("20대 입니다.")
    gender = input("성별을 입력하세요 예시 여/남:")
    if gender == "여":
        print("20대 여성입니다")
    else:
        print("20대 남성입니다")
elif age >=30 and age < 40:
    print("30대 입니다")
else:
    print("중년입니다")
print(f'나이는 {age}세 입니다')