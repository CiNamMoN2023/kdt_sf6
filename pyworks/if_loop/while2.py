#while True:무한 반복문, if _~break(빠져나옴)
'''
while True:
    lunch = input("오늘 점심 메뉴")
    print(lunch +'!!')
    if lunch == "그만":
        break
    print(lunch +"!!")
print("done")
'''

#1부터 10까지 출력하기
count = 0
while True:
    count = count + 1
    if count > 10:
        break
    print(count, end = " ") #end는 줄바꿈x

print("끝")


