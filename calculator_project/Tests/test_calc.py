from calculator_vw.calculator import Calculator

# Create an instance of the Calculator class
test_calculator = Calculator()

def test_add():
  assert test_calculator.add(4) == 4
  assert test_calculator.add(4) == 8

def test_reset():
  assert test_calculator.reset() == 0

def test_subtract():
  assert test_calculator.subtract(4) == -4
  assert test_calculator.subtract(4) == -8
  assert test_calculator.reset() == 0

def test_multiply():
  assert test_calculator.multiply(4) == 0
  assert test_calculator.add(10) == 10
  assert test_calculator.multiply(4) == 40
  assert test_calculator.reset() == 0

def test_divide():
  assert test_calculator.divide(4) == 0
  assert test_calculator.add(10) == 10
  assert test_calculator.divide(2) == 5
  assert test_calculator.reset() == 0

def test_nroot():
  assert test_calculator.nroot(1) == 0
  assert test_calculator.add(9) == 9
  assert test_calculator.nroot(2) == 3


if __name__ == "__main__":
  test_add()
  test_reset()
  test_subtract()
  test_multiply()
  test_divide()
  test_nroot()
  print("Everything passed")



