my_shop = ['반팔티','청바지','이어폰',['무선키보드','유선키보드']]
#이어폰 출력하기
print(my_shop[2])
print(my_shop[-1])

#'반팔티'를 '긴팔티'로 수정
my_shop[0] = '긴팔티'

print(my_shop[:])
print(my_shop[3])
# 이차원 리스트
print(my_shop[3][0])

#여러개 삭제
del my_shop[0:2] #0