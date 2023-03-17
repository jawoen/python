# ex06_lotto.py
# random모듈 불러오기
import random

# 로또번호 출력하기
lottolist = []
resultlist = []

for i in range(1,46):
    lottolist.append(i)
    
# 숫자 6개 추출하여 출력 --> resultlist
# [1,2,3,4,5,6,...45] --> 5 --> resultlist --> lottolist 5 제거

for i in range(6):
    # 1 ~ 45 lottolist 인덱스번호 0~44
    randomNum = random.randint(1,len(lottolist))-1
    lottol = lottolist.pop(randomNum)
    resultlist.append(lottol)
print(resultlist)
