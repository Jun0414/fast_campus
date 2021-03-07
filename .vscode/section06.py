# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#    code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요(호출보다 위에 선언)


# 예제1
def Hello(world):
    print('Hello', world)

Hello('Python!')
Hello(7777)

# 예제2
def hello_return(world):
    val = 'Hello' + str(world)
    return val

str = hello_return('Python!!')
print(str)

# 예제3(다중리턴)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val1, val2, val3)

# 예제4(데이터 타입 반환)
def func_mul2(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

lt = func_mul2(100)
print(type(lt), lt)

print()
print()


# 예제5
# 가변인자

# *args : 매개변수의 개수가 불분명할때(tuple형태로 받을때)
def args_func(*args):
    print(args) # 튜플로 출력
    for t in args: # 튜플형식 없이 값만 출력
        print(t)
    for i, v in enumerate(args): # 인덱스도 생성해준다
        print(i, v)

args_func('Kim')
args_func('Kim', 'Park')
args_func('Kim', 'Park', 'Lee')

print()
print()


# **kwargs : 매개변수의 개수가 불분명할때(dict형태로 받을때)
def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1='Kim')
kwargs_func(name1='Kim', name2='Park', name3='Lee')

print()
print()

# 혼합 사용
def example_func(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_func(10, 20)
example_func(10, 20, 'Park', 'Kim', name='Bong', phone='010')
# example_func(10, 20, 'Park', name='Bong', 'Kim', phone='010') *args와 **kwargs의 순서를 섞어서 사용할 수 없다

print()
print()


# 중첩함수(클로저)(파이썬 데코레이터 클로저)
def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print('in func')
    func_in_func(num + 10000)

nested_func(10000)

print()
print()


# 예제6
# (x : int) -> list      <x는 매개변수, : int는 매개변수의 자료형, -> list는 결과 자료형>

# 함수가 다른 파일에 있을때 hint를 주는 역할
# 어떤 타입의 매개변수를 받고 반환하는지
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3]

print(func_mul3(5))

print()
print()


# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap) 초기화 -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> list:
    return num * 10

# mul_10함수의 object를 할당 (함수object에 ()를 붙이면 함수 호출이 된다)
var_10 = mul_10
print(var_10)
print(type(var_10))

print(var_10(10))

# 람다식 사용
lambda_mul_10 = lambda num : num * 10

print('>>>', lambda_mul_10(10))

print()
print()


# 매개변수에 함수 사용
def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

# 람다를 즉시만들어 사용
func_final(10, 10, lambda x : x * 1000)