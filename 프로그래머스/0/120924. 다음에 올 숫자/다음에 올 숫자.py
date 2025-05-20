def solution(common):
    if common[1] - common[0] == common[2] - common[1]:
        diff = common[1] - common[0]
        return common[-1] + diff
    else:
        if common[0] == 0:
            # 등비 수열인데 첫 항이 0이면 판단 불가하거나 오류 가능
            raise ValueError("Cannot determine ratio for zero starting term in geometric sequence")
        ratio = common[1] // common[0]
        return common[-1] * ratio