"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0) :
        """"initializes a new serial and assigns a number for all methods to start from"""
        self.start = start
        self.next = start

    def __repr__(self) :
        """Show representation of class"""
        return f"<SerialGenerator start={self.start} next={self.next}"

    def generate(self) :
        """Will increase the origin of the instance by 1"""
        self.next += 1
        return self.next
    
    def reset(self) :
        """Will reset the origin to what it was when the instance was initialized"""
        self.next = self.start
        return self.next



