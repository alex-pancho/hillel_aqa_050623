import requests
import time

def decorator_function(func):
    def wrapper():
        print("obgortka")
        func()
        print("out")
    return wrapper


@decorator_function
def run():
    print("It is run!")

# run()

def benchmark(iters: int):

    def hilevel_decorator(func):

        def wrapper(*arg, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*arg, **kwargs)
                end = time.time()
                total_current = end - start
                print(f'[*] Час виконання: {total_current} секунд.')
                total = total + total_current
            print(f'[*] Середній час виконання: {total/iters} секунд.')
            return return_value

        return wrapper
    return hilevel_decorator

@benchmark(3)
def fetch_webpage(url: str):
    web_content = requests.get(url)
    return web_content.status_code

webpage = fetch_webpage('https://google.com')
print(webpage)


# def decor(func):
#     return func("Mary")


# @decor
# def print_hello(name):
#     print(f"Hello {name}!")

# print_hello

def decor(func):
    def wrapper(arg="Mary"):
        func(arg)
    return wrapper


@decor
def print_hello(name):
    print(f"Hello {name}!")

print_hello()
