class Guard:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', None)
        self.salary = kwargs.get('salary', 0)

    def greet(self):
        return f"Hello, my name is {self.name}!"

    def receive_bribe(self, num: int):
        if num > self.salary:
            return "You may pass."
        else:
            return "I am not letting you pass."
