import sys

class Redirect:
    def __init__(self, filepath, direct):
        self.filepath = filepath
        self.dir = direct
        self.o = sys.stdout
        self.e = sys.stderr

    def __enter__(self):
        self.f = open(self.filepath, 'a')
        if self.dir == 'o':
            sys.stdout = self.f
        if self.dir == 'e':
            sys.stderr = self.f
        if self.dir == 'oe':
            sys.stdout = self.f
            sys.stderr = self.f
        return self.f

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_value:
            print('exit exception text: %s' % exc_value)
            return True
        sys.stdout = self.o
        sys.stderr = self.e
        self.f.close()
