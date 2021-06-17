class Knight:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def greet(self):
        if hasattr(self, 'name') and hasattr(self, 'title'):
            print(f"Hello, I'm Sir {self.name} the {self.title}!")
        else:
            print("Hello!")
