# Awesome

- [Five whys](https://en.wikipedia.org/wiki/Five_whys)
- [Six Myths of Product Development](https://hbr.org/2012/05/six-myths-of-product-development)
- [Super Chicken - Margaret Heffernan TED Talk](https://www.youtube.com/watch?v=udiTaS2wTAM)
- [Six Sigma](https://en.wikipedia.org/wiki/Six_Sigma)

## Agile engineering to win the human powered helicopter flight challenge?

The whole helicopter was built like a house of cards, so when one
thing went wrong, the entire thing fell apart[2]. AeroVelo Inc. used agile
engineering to design parts that could easily be put back together after
breaking[2]. This helped them win the human-powered helicopter flight
challenge[2][3].


- https://www.machinedesign.com/automation-iiot/article/21834328/inside-the-sikorsky-prizewinning-humanpowered-helicopter
- https://www.cnn.com/2013/12/17/tech/innovation/ideas-aerovelo-human-power/index.html
- https://interestingengineering.com/innovation/aerovelos-human-powered-helicopter-wins-250000-prize

## My take on S.O.L.I.D principles

### S.O.L.I.D principles  

- Single-responsibility principle - no stepping on toes when fixing two issues
- Open–closed - OO inheritance and composition mixins
- Liskov substitution - stick the client interface
- Interface segregation principle (ISP)
- Dependency inversion principle

### Distilling S.O.L.I.D down to "interface design principles'

Design your interface for a near future of continuous improvement 

Assume future failure that will need continuous improvement (CI), so upfront invest in reducing the growth of extraneous cognitive load so you have a clear road to the anticipated CI ...."its not the distance, its the pebble in your shoe" 

Christopher Alexander "A Pattern Language" on Interface

Principles of good interface design

- Interface layer - CI design
  - Stable - Liskov substitution - (generalize customer interaction) - Mix and Match
  - flexible (generalize classes - extend classes over changing code) - Mix and Match
  - ISP or minimal clean interface for customer to understand - Mix and Match
  - Swap out low level service using an interface layer - Mix and Match
- CI process (ABC): split classes/services or decouple jobs (divide and conquer), scale human cognition, reduce extraneous cognitive loads

No-technical synonyms

Mix and Match - Creativity space and the cost of execution speed - Counter factual reasoning - lower the cost of experimenting - dont trap yourself in a golden jail - opening chess move 

### Others 

- [Principles for Microservice Design: Think IDEALS, Rather than SOLID](https://www.infoq.com/minibooks/reexamining-microservices/)

### Single-responsibility principle - don't step on each other's toes

[wiki: Single-responsibility principle](https://en.wikipedia.org/wiki/Single-responsibility_principle)

Your television and your computer screen have different jobs, they serve
different roles.

You don't want the person improving your television to be stepping on the toes
of the person improving your computer screen. You don't want a bug or regression
in your television to spillover and break your computer screen. Therefore, you
have two classes instead of one, even though its tempting to consolidate them
because they look alike.


### Nail down your interface

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

# Interesting readings

- Loonshots
- Innovation Stack 
- [Are You Solving the Right Problem?](https://hbr.org/2012/09/are-you-solving-the-right-problem)

# cognitive load theory and making software

- extraneous cognitive load versus other types
- confusing extraneous cognitive load for intrinsic load to learn
- naming to reduce
- interface to reduce
- always putting our fire, can't make the design leap
- hidden scripts
- layers of abstraction that obfuscate 
- No reward for tiny actions to reduce load versus being system debugging hero
- Design documentation
- Communication with same language
- The "craft" of software


# Data side versus algorithm side 


- finding alpha - economic value from re-conceptualizing what the data means
- risky (engineering) versus frisky (data side)
- represent info value via data structure - simplification 
- enormous cognitive load up front to reduce long term load ...the sorting for BIG O problem for the human brain... 
- ROI
- Data design to reduce cognitive load and scale humans
- A computational model of human cognitive load

# References 

- Cognitive load during problem solving: Effects on learning
- Cognitive load measurement as a means to advance cognitive load theory
- Cognitive load while learning to use a computer program
- Evidence for cognitive load theory

# The dilemma 

Make a link to Loonshot book's theory

- questioning will come at the cost of the perception of execution speed at the
  benefit of avoiding the XY problem and making a Rube Goldeberg machine -- this
  will be hard without circumventing the conventional hierarchy that instills
  fear to keep the perception of execution speeds high.
