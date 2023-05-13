def hello():
    print('Heloooooooooooooooo')


greet = hello
del hello

print(greet())


# Higher Order Functions - HOF - any func that accepts another func as param or returns a func. As map() function:
def greet(func):
    func()


def greet2():
    def func():
        return 5

    return func


# ----------------------------------------------------------------

def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')

    return wrap_func


@my_decorator
def hello():
    print('Hello')


@my_decorator
def bye():
    print('see ya later')


def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('******')
        func(*args, **kwargs)
        print('******')

    return wrap_func


@my_decorator2
def hello2(greeting, emoji=': )'):
    print(greeting, emoji)


hello2('hi')

# Homework

# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True  # changing this will either run or not run the message_friends function.
}


def authenticated(fn):
    def wrapper_func(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)

    return wrapper_func


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)
