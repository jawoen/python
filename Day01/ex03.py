str = "hobby"
# 문자 개수 문자열.count('찾는문자')
print(str.count('b'))
# 위치 찾기 fine
print(str.find('z'))
# 위치 찾기 index
# print(str.index('z'))
# 문자열 삽입 join
print("*".join('green'))
# 리스트 --> 문자열로 반환
print("*".join(['a','b','c','d','e']))
# 대문자 upper()
str2 = "abcde"
print(str2.upper())
# 소문자 lower()
str3 = "ABCDE"
print(str3.lower())
# 공백지우기 왼쪽 lstrip(), 오른쪽 rstrip(), 양쪽 strip()
str4 = "    안녕하세요   "
print(str4.lstrip())
print(str4.rstrip())
print(str4.strip())