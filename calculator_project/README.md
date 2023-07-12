# Calculator Project

This calculator is a tool with which you can use calculation functions sequentially, with a resettable memory. 

## Installation 

pip install -i https://test.pypi.org/simple/ calculator-vw==0.0.1

## Usage 

By importing the calculator_vs package and module you will be able to make use of the following functions:

.add() 
.subtract() 
.divide() 
.multiply() 
.nroot()
.reset()

The above functions only require one number as an input and will perform a calculation with that, based on the outcome of the previous calculation, the memory. 
For example: calculator.add(4) will add 4 to the current memory value.
When creating an instance of the Calculator class, the memory, and thus the number that your calculator object will start calculating from, will by default be zero. This means that in the example above, when it is the first calculation after creating an instance, it will return 4. 
You can choose to set a different starting number, by inputting the desired starting number between () when creating an instance of the Calculator class.

You can use the functions above to cumulatively calculate, as it memorizes the outcome of your previous calculation(s). Thus in the above described example, when subsequently specifying calculator.subtract(2), it will return 2. 
If you want to clear the memory, you can use .reset() to start from zero again.

Keep in mind that when the first calculation function used, will be any other than .add, the outcome will be zero (as zero multiplied, divided or nth root of zero returns zero), or when starting with .subtract, the outcome will be negative.

Users can input decimal and integer numbers.

## License

This project is licensed under the MIT License. See the LICENSE file for more information.