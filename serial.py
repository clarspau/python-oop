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

    def __init__(self, start=0):
        """Create a new Serial Generator, provide the starting number."""

        self.start = self.next = start

    def __repr__(self):
        """show string representation."""

        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        """Generate and return the next serial number."""

        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset the serial number to the original start number."""

        self.next = self.start
