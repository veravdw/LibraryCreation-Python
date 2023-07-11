"""This Module contains one Calculator class and several functions to perform
basic calculations of addition, subtraction, multiplication, division and nth root
with a memory that is resettable. 
"""

class Calculator:

  def __init__(self, memory=0):
    """Constructor for the Calculator class.

    Attributes:
      Memory: starting number for calculations by default zero, but can be set to a 
      different number by the user when creating an instance of the Calculator class.
      The memory 
      keeping every previous outcome as a base for the next calculation function 
      used sequentially until reset. 
    """
    self.memory = memory

  def add(self, number_input: float):
    """Add input number up to memory."""
    self.number_input = number_input
    self.memory = self.memory + self.number_input
    return self.memory

  def subtract(self, number_input: float):
    """Subtract input number from memory."""
    self.number_input = number_input
    self.memory = self.memory - self.number_input
    return self.memory

  def multiply(self, number_input: float):
    """Multiply memory by input number."""
    self.number_input = number_input
    self.memory = self.memory * self.number_input
    return self.memory

  def divide(self, number_input: float):
    """Divide memory by input number."""
    self.number_input = number_input
    self.memory = self.memory / self.number_input
    return self.memory

  def nroot(self, number_input: float):
    """Take the input number's root of the memory."""
    self.number_input = number_input
    self.memory = self.memory**(1/self.number_input)
    return self.memory

  def reset(self, memory=0):
    """Reset the memory attribute to zero to start calculating
    from zero again
    """
    self.memory = memory
    return self.memory



