#https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    completion.sort()
    participant.sort()
    
    for i in completion:
        participant.remove(i)

    return participant[0]
  
  #테스트 케이스에 대한 값은 정상적으로 풀렸지만
  #효율성 측면에서 한개만 통과되는 좋지않은 효율을 보였다.
  #2021.06.02
  #채점 결과
  #정확성: 50.0
  #효율성: 10.0
  #합계: 60.0 / 100.0

import collections
def solution(participant, completion):
    answer = ''
    ct1 = collections.Counter(participant)
    ct2 = collections.Counter(completion)
    return list(ct1 - ct2)[o]

#collection 패키지를 이용하니 금세 풀렸다.
