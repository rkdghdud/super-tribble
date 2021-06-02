def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            return False

    return True
  #전화번호를 오름차순으로 정렬하면 크기순으로 정렬된다는 생각으로 진행하였다.
  #또한 한 번호가 다른 번호의 접두사가 된다는 점으로 비교를 할때 슬라이스하여 비교하였다.
