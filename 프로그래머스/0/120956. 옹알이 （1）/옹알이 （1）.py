# 정규 표현식 패턴 정의
# ^(aya|ye|woo|ma)+$
# aya, ye, woo, ma 네 개 중 하나가 반복적으로 등장하는 경우만 허용합니다.
# ^와 $를 사용하여 문자열 전체가 해당 패턴과 일치해야 합니다.
# 예를 들어, "ayaye"는 가능하지만 "woowo"처럼 중간에 다른 문자가 포함되면 안 됩니다.

# 문자열 검사 (re.fullmatch)
# re.fullmatch(pattern, word)는 word가 pattern과 완전히 일치할 때만 True를 반환합니다.
# "ayaye" → True
# "woowo" → False
# "maaya" → False (순서가 바뀌면 불가능)
# 일치하는 단어 개수 세기

# count 변수를 사용하여 pattern.fullmatch(word)가 True인 경우 카운트 증가.

import re    

def solution(babbling):
#     pattern = re.compile(r"^(aya|ye|woo|ma)+$")
#     invalid_pattern = re.compile(r"(ayaaya|yeye|woowoo|mama)")
#     answer = 0

#     for word in babbling:
#         if pattern.fullmatch(word) and not invalid_pattern.search(word):
#             answer += 1
    
    answer = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, " ") # 단순히 지워버리면 중간에 들어간 부분이 지워진 다음 이어진 단어가 4단어에 포함되는 경우 제대로 걸러내지 못하는 경우가 생길 수 있음
        if len(b.strip()) == 0:
            answer += 1
    
    return answer