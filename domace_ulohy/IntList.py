class IntList(list):
    def __init__(self, *args):
        for arg in args:
            if not all(isinstance(item, int) for item in arg):
                raise ValueError("All values must be integers")
        super().__init__(*args)

    def append(self, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        super().append(value)

    def extend(self, values):
        for value in values:
            if not isinstance(value, int):
                raise ValueError("All values must be integers")
        super().extend(values)

    def __setitem__(self, index, value):
        if not isinstance(value, int):
            raise ValueError("Value must be an integer")
        super().__setitem__(index, value)
