# https://programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement

def get_score(a, r):
    a_score = 0
    r_score = 0
    
    for i in range(len(a)):
        if a[i] > 0 or r[i] > 0:
            if a[i] >= r[i]:
                a_score += (10-i)
            else:
                r_score += (10-i)
    
    return a_score, r_score


def solution(n, info):
    score_list = [i for i in range(11)]
    r_scores = list(combinations_with_replacement(score_list, n))
    
    max_score = 0
    answer = None 
    for r_score in r_scores:
        r = [0] * 11
        for i in r_score:
            r[10-i] += 1

        a_score, r_score = get_score(info, r)
        if r_score > a_score and (r_score - a_score) > max_score:
            max_score = r_score - a_score
            answer = r
                
    return answer if answer else [-1]