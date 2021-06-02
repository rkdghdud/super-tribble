#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = {}
    
    for i in clothes:
        if i[1] in answer: answer[i[1]] += 1
        else: answer[i[1]] = 1
    count = 1
    
    for i in answer:
        count *= answer[i] + 1
    
    return count - 1
  
  #(의상종류별 갯수 + 1) * (의상종류별 갯수 + 1) * ... * (의상종류별 갯수 + 1) - 1
