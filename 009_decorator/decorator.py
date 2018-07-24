class WindowInterface:
    def build(self): pass


class AbstractWindowDecorator(WindowInterface):
    """
    Maintain a reference to a Window object ad define an interface
    that conforms to Window's interface.
    """
