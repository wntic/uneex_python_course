class Mixed:
    def __init__(self, *objects):
        for obj in objects:
            for attr in dir(obj):
                if not attr.startswith("_"):
                    value = getattr(obj, attr)
                    if not callable(value):
                        setattr(self, attr, value)

    def __str__(self):
        attrs = {k: v for k, v in self.__dict__.items()}
        sorted_attrs = sorted(attrs.items())
        return ", ".join(f"{k}={v}" for k, v in sorted_attrs)


def mix(*objects):
    return Mixed(*objects)
