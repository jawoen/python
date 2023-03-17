# True, False만 나타내는 자료형
# 자료형의 참과 거짓 구분하기
# 문자열 -> 빈문자열 : 거짓, "a" : 참
# 리스트, 딕셔너리, 튜플 -> 비어져있으면 : 거짓,
# 요소가 있으면 참
# 숫자 1 : 참 , 0 : 거짓
# None : 거짓
# 문자열, 리스트, 딕셔너리, 튜플 값이 비어있으면 거짓
# bool(value) --> 불타입으로 변환
print(bool(0))      #False
print(bool(-1))     #True
print(bool(""))     #False
print(bool(" "))    #True
print(bool("aaa"))  #True
print(bool([]))     #False
print(bool({}))     #False
print(bool(()))     #False

# 1.
pin = "881120-16068234"
print(pin[7])

# 2.
a = "a:b:c:d"
b = (a.replace(":","#"))
print(b) 

# 3.
list1 = [1,3,5,4,2]
list1.sort()
print(list1)

# 4.
list1.reverse()
print(list1)

# 5.
list2 = ["life","is","too","short"]
result = (" ".join(list2))
print(result)

# 6.
list3 = [1,1,1,2,2,2,3,3,4,4,5,5,6]
setlist3 = set(list3)
list4 = list(setlist3)
print(list4)