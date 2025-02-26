def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        deploy = 0
        while progresses and progresses[0] >= 100:
            deploy += 1
            del progresses[0]
            del speeds[0]
        if deploy > 0:
            answer.append(deploy)
    return answer