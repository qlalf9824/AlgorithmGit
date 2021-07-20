def solution(phone_book):
    answer = True
    phone_book.sort()
    print(phone_book)
    before = " "
    for i in range(len(phone_book)):
        if(phone_book[i].startswith(before)):
            return False
        before = phone_book[i]
 
    return answer

print(solution(["12","123","1235","567","88"]))