# single object initiation


class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


borg1 = Borg()
borg2 = Borg()

print(borg1 == borg2)
borg1.val = 'test'
print(borg2.val)
