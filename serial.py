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
    def __init__(self, start, serial=0):
        self.start = start
        self.serial = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}, next={self.serial+1}>"
    
    def generate(self):
        """ Generate unique incrementing serial number """
        self.serial += 1
        return self.serial - 1
    
    def reset(self):
        """ Reset serial number to start"""
        self.serial = self.start


