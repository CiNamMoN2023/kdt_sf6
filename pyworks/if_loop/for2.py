#for in 리스트
shop = ['반팔티','바지','이어폰','키보드']
print('바지' in shop ) #True
print('양말' in shop ) #False

shop.append('마우스')
#for 문을 써서 모든 값 출력하는 방법
for i in shop:
    print(i)
#그냥 평소대로 출력
print(shop[:])
#"이어폰"값 삭제
shop.remove('이어폰')
shop.extend(['커피','바스켓']) #두개 값 더하기
# 만약 두개이상 값 빼려면 del 기억나지?

print(shop[:])

#리스트의연산
#개수, 합계, 평균, 최대값, 최소값
score = [70,80,60,90,40]

print(f'리스트 개수는:{len(score)}')
print(f'리스트 합계는:{sum(score)}')
print(f'리스트 평균은:{sum(score)/len(score)}')
print(f'리스트 최대값은:{max(score)}')
print(f'리스트 최솟값은:{min(score)}')

#합계
sum_v = 0
for i in score:
    sum_v = sum_v + i
print(f'합계:{sum_v}')


#최대값
max_v = score[0] #처음 값으로 초기화
n = len(score)
for i in range(1,n): #n+1이 아닌 n으로 , 왜냐면 배열이니깐
    if score[i] > max_v:
        max_v = score[i]
print(f'최대값:{max_v}')
# 또 다른 방법
max_v = -99 #매우 작은 값으로 초기화
for i in score: #i -리스트의 요소
    if i > max_v:
        max_v = i
print(f'최대값')

