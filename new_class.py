#!/usr/bin/python
from parentclass import Parent;
class new_class:
    def __init__(self):
        print("in new_class constructor");

    def getNewThings(self, first_param, second_param=None):
        if ( second_param is None ):
            print("Second param is not passed. first_param value = ", first_param);
        else:
            print("Second param value is passed. first_param value =", first_param,": second_param value = ", second_param);

### Calling a differnt methods of different class from this class
parentclass = Parent();
print("before setting the attr value:: ")
parentclass.getAttr();
parentclass.setAttr(300);
print("after setting the attr value to 300:: ")
parentclass.getAttr();

newclass = new_class();
newclass.getNewThings(30);
newclass.getNewThings(30, 40);
