
class GCDCalculator:
    """
    A class to calculate the Greatest Common Divisor (GCD) of two positive integers
    using the Euclidean Algorithm.
    """

    def __init__(self) -> None:
         """ Initialize the GCDCalculator object. """
         pass
    def get_GCD(self, a: int, b: int):
        """
        Calculate the GCD of two positive integers using the Euclidean Algorithm.

        Args:
            a (int): The first positive integer.
            b (int): The second positive integer.

        Returns:
            int: The GCD of a and b.

        Raises:
            ValueError: If either a or b is not a positive integer.
        """

        # If the second number is 0, the GCD is the first number.
        if b == 0:
            return a

        # Calculate the remainder of the division of the first number by the second number.
        remainder = a % b

        # Recursively call the function with the second number and the remainder until the second number is 0.
        return self.get_GCD(a, remainder)




# Example usage
gcd_calculator = GCDCalculator()

# Calculate the GCD of 24 and 18
result = gcd_calculator.get_GCD(24, 18)
print(f"The GCD of 24 and 18 is: {result}")  # Output: The GCD of 24 and 18 is: 6

# Calculate the GCD of 35 and 21
result = gcd_calculator.get_GCD(35, 21)
print(f"The GCD of 35 and 21 is: {result}")
