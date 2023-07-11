from calculator_vw import calculator 

# Creating an instance of Calculator()
test_calculator = calculator.Calculator()

# test addition from zero and memory
assert test_calculator.add(4) == 4
assert test_calculator.add(4) == 8

# test reset
assert test_calculator.reset() == 0

# test subtraction
assert test_calculator.subtract(4) == -4
assert test_calculator.subtract(4) == -8
assert test_calculator.reset() == 0

# test multiplication
assert test_calculator.multiply(4) == 0
assert test_calculator.add(10) == 10
assert test_calculator.multiply(4) == 40
assert test_calculator.reset() == 0

# test division
assert test_calculator.divide(4) == 0
assert test_calculator.add(10) == 10
assert test_calculator.divide(2) == 5
assert test_calculator.reset() == 0

# test nroot
assert test_calculator.nroot(0) == 0
assert test_calculator.add(9) == 9
assert test_calculator.nroot(2) == 3

# test combination
assert test_calculator.add(17) == 20
assert test_calculator.multiply(4) == 80
assert test_calculator.divide(2) == 40
assert test_calculator.subtract(20) == 20



