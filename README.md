🌡️ Temperature Converter
Python
Beginner
Variables & Input
01_variables_input
A Python command-line program that converts a temperature value between Celsius, Fahrenheit, and Kelvin.

📋 Problem Statement
Accept a temperature value and its unit as input, then output the equivalent values in all three temperature units.

💡 Concepts Used
Functions
One per conversion pair
User Input
input() + type casting
Conditionals
if / elif branching
Formatting
f-strings + :.2f
🚀 How to Run
Terminal
python temperature_converter.py
📥 Sample Input / Output
📥 Input
Enter Temperature Value: 100
Enter Unit (C/F/K): C
📤 Output
Celsius   : 100.00 °C
Fahrenheit: 212.00 °F
Kelvin    : 373.15 K
🧮 Formulas Used
Conversion	Formula
Celsius → Fahrenheit	(C × 9/5) + 32
Celsius → Kelvin	C + 273.15
Fahrenheit → Celsius	(F − 32) × 5/9
Fahrenheit → Kelvin	Convert to °C first, then to K
Kelvin → Celsius	K − 273.15
Kelvin → Fahrenheit	Convert to °C first, then to °F
🧪 Test Cases
Input	Unit	Celsius	Fahrenheit	Kelvin
100	C	100.00	212.00	373.15
32	F	0.00	32.00	273.15
0	K	−273.15	−459.67	0.00
📂 Repository Structure
python-fundamentals-practice/
└── 01_variables_input/
    ├── temperature_converter.py
    └── README.html
Part of python-fundamentals-practice — solved as part of Python Fundamentals practice before moving into Python Data Science.
