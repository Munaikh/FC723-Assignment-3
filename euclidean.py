class GCDCalculator:
    """
    A class to calculate the Greatest Common Divisor (GCD) of two positive integers
    using the Euclidean Algorithm.
    """

    def __init__(self) -> None:
        """Initialize the GCDCalculator object."""
        pass

    # Make the function static so that you can access it without creating an object
    @staticmethod
    def get_GCD( a: int, b: int):
        """
        Calculate the GCD of two integers using the Euclidean Algorithm.

        Args:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The GCD of a and b.

        Raises:
            ValueError: If either a or b is not an integer.
        """
        # Check if a and b are integers
        if not (isinstance(a, int) and isinstance(b, int)):
            raise ValueError("Both inputs must be integers.")

        # If the second number is 0, the GCD is the first number.
        if b == 0:
            return a

        # Calculate the remainder of the division of the first number by the second number.
        remainder = a % b

        # Recursively call the function with the second number and the remainder until the second number is 0.
        return GCDCalculator.get_GCD(b, remainder)


while True:
    try:
        # Ask the user for input
        a = (input("Enter the first positive integer (or 'q' to quit): "))
        if a == "q":
            break
        b = (input("Enter the second positive integer: "))

        # Calculate the GCD
        result = GCDCalculator.get_GCD(int(a), int(b))
        print(f"The GCD of {a} and {b} is: {result}")

    except ValueError:
        print("Invalid input. Please enter integers only.")
        continue
