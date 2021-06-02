def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            return False

    return True
  #전화번호를 오름차순으로 정렬하면 크기순으로 정렬된다는 생각으로 진행하였다.
  #또한 한 번호가 다른 번호의 접두사가 된다는 점으로 비교를 할때 슬라이스하여 비교하였다.

def solution(phone_book):
    phone_book.sort()
    
    for i,j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True

#마찬가지로 정렬후 각각 한 전화번호와 그다음 번호를 호출하고 startswith 메소드로 두어를 검사하는 방법이다.
