class Person0:
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job

p1 = Person0('Adam', 'Sidorenko', 30, 'scientist')
print(p1.age)










from dataclasses import dataclass, asdict, astuple


@dataclass
class Person:
    first_name: str = 'Name'
    last_name: str = 'Surname'
    age: int = 30
    job: str = 'Engineer'


p = Person()
print(p)
print(p.age)
# p.age = 25
print(asdict(p))
print(astuple(p))
p2 = Person()
print(p == p2)


@dataclass(frozen=True)
class Person2:
    first_name: str = "Adam"
    last_name: str = "Sidorenko"
    age: int = 30
    job: str = "Data Scientist"

    def __post_init__(self):
        print('Post init block')


p2 = Person2(first_name='Petro', age=25)
#p2.age = 25
print(p2)
