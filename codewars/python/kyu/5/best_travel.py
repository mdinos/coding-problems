# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

from itertools import combinations

def choose_best_sum(t, k, ls):
    any_len_combos = [combo for i in range(k) for combo in combinations(ls, i + 1)]
    combos = [combo for combo in any_len_combos if len(combo) >= k]
    sums = []
    for combo in combos:
        sums.append(sum(combo))
    sums = [sum for sum in sums if sum <= t]
    if len(sums) > 0:
        return(max(sums))
    else:
        return None