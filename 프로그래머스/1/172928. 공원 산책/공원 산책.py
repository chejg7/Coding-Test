def solution(park, routes):
    # 시작 위치 찾기
    i, j = 0, 0
    for row in range(len(park)):
        if "S" in park[row]:
            i, j = row, park[row].index("S")
            break

    for route in routes:
        direction, distance = route.split(" ")
        distance = int(distance)
        ni, nj = i, j  # 이동할 위치 초기화
        ver = []  # 장애물 체크 리스트 초기화

        if direction == "E":
            nj = j + distance
        elif direction == "W":
            nj = j - distance
        elif direction == "S":
            ni = i + distance
            if ni < len(park):  # 범위 체크
                for k in range(i, ni + 1):
                    ver.append(park[k][j])
        elif direction == "N":
            ni = i - distance
            if ni >= 0:  # 범위 체크
                for k in range(ni, i + 1):
                    ver.append(park[k][j])

        # 이동 후 범위 검사
        if ni < 0 or ni >= len(park) or nj < 0 or nj >= len(park[0]):
            continue

        # 장애물 검사
        if "X" in ver or "X" in park[i][min(j, nj): max(j, nj) + 1]:
            continue

        # 위치 업데이트
        i, j = ni, nj

    return [i, j]
