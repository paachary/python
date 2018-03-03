# Inheritance example
from parentclass import Parent


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method
