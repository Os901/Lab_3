x = int(input("Enter a number of repetitions: "))


def repeat_hello(func):
    def wrapper():
        for _ in range(x):
            func()
    return wrapper


def hello():
    print('Hello')


hello = repeat_hello(hello)


hello()