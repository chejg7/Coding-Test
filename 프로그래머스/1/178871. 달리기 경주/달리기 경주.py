# def solution(players, callings):
#     idx = {}
    
#     for c in callings:
#         if c in idx:
#             i = idx[c]
#         else:
#             i = players.index(c)
#             idx[c] = i
            
#         players[i - 1], players[i] = players[i], players[i - 1]
#         idx[c] = i - 1
#         idx[players[i]] = i
        
#     return players

# 인덱스를 찾기 위해 매번 리스트를 검색하므로 시간 효율성이 떨어짐.
# 처음부터 각 선수들의 이름과 순위를 딕셔너리에 넣고, 순위만 지속적으로 업데이트하는 방식으로 풀어야 함. 

def solution(players, callings):
    idx = {name: rank for rank, name in enumerate(players)}
    
    for c in callings:
        i = idx[c]
        players[i - 1], players[i] = players[i], players[i - 1]
        idx[c] = i - 1
        idx[players[i]] = i
        
    return players