#def 함수이름 (매개변수) :
#   함수에서 실행할 내용

def Hello(): #함수의 정의
    print("안녕하세요, 반갑습니다.") #함수 내용


Hello()
Hello()
Hello()

def add_numbers(a, b):
    result = a+b
    print(result)
    return result


a = add_numbers(5, 3)