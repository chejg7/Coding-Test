def solution(schedules, timelogs, startday):
    answer = 0
    
    for schedule, timelog in zip(schedules, timelogs):
        day = startday
        time = schedule + 10
        hour = (time // 100) + ((time % 100) // 60)
        minute = (time % 100) % 60
        time = hour * 100 + minute
        answer += 1
        for i in range(7):
            if day != 6 and day != 7 and timelog[i] > time:
                answer -= 1
                break
            day = (day % 7) + 1

    return answer