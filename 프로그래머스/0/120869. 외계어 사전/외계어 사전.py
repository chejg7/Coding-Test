def solution(spell, dic):
    spell_sorted = sorted(spell)
    for d in dic:
        word = sorted(list(d))
        if spell_sorted == word:
            return 1
            
    return 2