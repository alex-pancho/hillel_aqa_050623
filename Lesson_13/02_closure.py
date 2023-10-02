def hello(name):
    def formatted_hello():
        print(f'I wish to say hello to "{str(name).capitalize()}"')

    formatted_hello()


hello('adam')


def hello_closure(name):
    def formatted_hello():
        print(f'I wish to say hello to "{str(name).capitalize()}"')

    return formatted_hello


func = hello_closure('Bob')
func()


#
#
# # object exist so internal operates with external function and all related parameters

def count(start=0):
    def step():
        nonlocal start
        start += 1
        return start

    return step


c1 = count(start=100)
c2 = count(start=200)
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
print(c1(), c2())
#
# # more examples
