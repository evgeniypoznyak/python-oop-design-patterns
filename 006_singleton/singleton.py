# single object creation


class Singleton:
    __instance = None

    # overwriting object creation method
    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


s = Singleton()
s.val = 'test'
print(s.val)

s2 = Singleton()
s2.val = 'new value'
print(s2.val)

print(s.val)
