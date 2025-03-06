# def solution(scoville, K):
#     answer = 0
#     scoville.sort()
#     while len(scoville) > 1 and scoville[0] < K:
#         scoville[1] = scoville[0] + (scoville[1] * 2)
#         answer += 1    
#         del scoville[0]
        
#     return answer if scoville[0] >= K else -1

# 이 코드의 문제점 : 단순히 정렬한 뒤 첫 요소와 두번째 요소를 섞게 되면 제대로 정렬된 상태를 유지하지 못하는 문제가 있다. 매번 전체 리스트에서 스코빌 지수가 가장 작은 것과 두번째로 작은 것을 선택해야 하기 때문에 매번 정렬을 새로 해야 하는 것. -> 시간 효율성 문제

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 최소 힙 생성
    answer = 0

    while len(scoville) > 1 and scoville[0] < K:
        first = heapq.heappop(scoville)  # 가장 작은 값 추출
        second = heapq.heappop(scoville)  # 두 번째로 작은 값 추출
        new_scoville = first + (second * 2)  # 새로운 음식 만들기
        heapq.heappush(scoville, new_scoville)  # 다시 힙에 삽입
        answer += 1

    return answer if scoville[0] >= K else -1  # K 이상이 되지 않으면 -1 반환