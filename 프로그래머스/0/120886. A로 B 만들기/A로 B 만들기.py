def solution(before, after):
    before = list(before)
    after = list(after)
    for b in before:
        if b in after:
            del after[after.index(b)]
    return 1 if len(after) == 0 else 0