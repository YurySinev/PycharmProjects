#
class ParentClass:
    @classmethod
    def method(cls, arg):
        print("%s: classmethod.%d" % (cls.__name__, arg))
    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)

class ChildClass(ParentClass):
    @classmethod
    def call_original_method(cls):
        cls.method(6)

# ParentClass.method(0)
# ParentClass.call_original_method()
# ChildClass.method(0)
# ChildClass.call_original_method()
#
# my_obj = ParentClass()
# my_obj.method(1)
# my_obj.call_original_method()
# my_obj.call_class_method()