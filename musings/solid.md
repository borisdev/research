# S.O.L.I.D

- Single-responsibility principle - no stepping on toes when fixing two issues
- Open–closed - OO inheritance and composition mixins
- Liskov substitution - stick the client interface
- Interface segregation principle (ISP)
- Dependency inversion principle

# Alternatives

## Boris's - assume future failure will need CI, so reduce extraneous cognitive load for CI 

- Interface layer - CI design
  - Stable - Liskov substitution - (generalize customer interaction) - Mix and Match
  - flexible (generalize classes - extend classes over changing code) - Mix and Match
  - ISP or minimal clean interface for customer to understand - Mix and Match
  - Swap out low level service using an interface layer - Mix and Match
- CI process (ABC): split classes/services or decouple jobs (divide and conquer), scale human cognition, reduce extraneous cognitive loads

No-technical synonyms

Mix and Match - Creativity space and the cost of execution speed - Counter factual reasoning - lower the cost of experimenting - dont trap yourself in a golden jail - opening chess move 

## Others 

- [Principles for Microservice Design: Think IDEALS, Rather than SOLID](https://www.infoq.com/minibooks/reexamining-microservices/)

## Single-responsibility principle - don't step on each other's toes

[wiki: Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)

Your television and your computer screen have different jobs, they serve
different roles.

You don't want the person improving your television to be stepping on the toes
of the person improving your computer screen. You don't want a bug or regression
in your television to spillover and break your computer screen. Therefore, you
have two classes instead of one, even though its tempting to consolidate them
because they look alike.


## Nail down your interface

The Open-closed principle is an implementation pattern for the Liskov design principle.

### Liskov substitution principle

The dilemma is that want to continuously improve your service, but you don't
want to deal with its expensive implications of continuously changing the clients of your
service because your changes break its interface.

Starbucks continuously makes new drinks for its customers, but each new drink
has the same packaging interface so customers never get confused.

ChatGPT: "liskov substitution principle python" returned ...

```
class Animal:
    def __init__(self):
        pass

class Dog(Animal):
    def bark(self):
        print("Woof!")

class Cat(Animal):
    def meow(self):
        print("Meow!")

def make_noise(animal):
    animal.bark()
    animal.meow()

dog = Dog()
cat = Cat()

make_noise(dog) # Woof!
make_noise(cat) # Meow!
```


#### Open–closed principle - continuously improve but never change interface


[wiki Open–closed principle](https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle)

Design your class so you can extend it easily instead rather than change its code. In other words,
build a nice primitive in anticipation of future changes. 

Python tools for doing this:

- Abstract Bases Classes
- Inheritance
- Mixing features with Mixin Classes

#### ISP - Interface Segregation Principle - minimalism to reduce client's cognitive load - class composition  

[Reasons to Follow the Interface Segregation Principle](https://reflectoring.io/interface-segregation-principle/)

#### Dependency inversion principle - swap out low level services by using an interface layer
