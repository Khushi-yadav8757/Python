#Difference between __str__ and __repr__?
Ans:-
__str__: User-friendly (used by print).
__repr__: Developer-friendly (used in shell).

class Person:
    def __str__(self):
        return "Person object"
    def __repr__(self):
        return "Person(name)"
