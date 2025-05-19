# Procedural style
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

# OOP style
class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

g = Greeter("Bob")
g.greet()
