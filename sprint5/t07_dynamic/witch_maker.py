class Witch:
    def __init__(self, name=None):
        self.name = name

def get_witch_class(class_name, specialty, skills):
    new = type(class_name, (Witch, ), dict(specialty=specialty))
    for method in skills:
        setattr(new, method.__name__, method)
    return new
