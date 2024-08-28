class Python:
    staticVariable = 5

    @classmethod
    def modify_static_variable(cls, value):
        cls.staticVariable = value
        print(f"Class-level staticVariable changed to: {cls.staticVariable}")

    def __init__(self):
        self.instanceVariable = Python.staticVariable

    def modify_instance_variable(self, value):
        self.instanceVariable = value
        print(f"Instance-level instanceVariable changed to: {self.instanceVariable}")

# Access the static variable through the class
print(f"Initial class-level staticVariable: {Python.staticVariable}")

# Modify the static variable using a class method
Python.modify_static_variable(60)

# Access the static variable through an instance
instance = Python()
print(f"Instance-level staticVariable: {instance.instanceVariable}")

instance.modify_instance_variable(55)

print(f"Class-level staticVariable remains: {Python.staticVariable}")
