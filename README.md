<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Temperature Converter — README</title>
 
</head>
<body>
<div class="container">
 
  <h1>🌡️ Temperature Converter</h1>
 
  <div class="badge-row">
    <span class="badge b-blue">Python</span>
    <span class="badge b-green">Beginner</span>
    <span class="badge b-amber">Variables & Input</span>
    <span class="badge b-gray">01_variables_input</span>
  </div>
 
  <p>A Python command-line program that converts a temperature value between Celsius, Fahrenheit, and Kelvin.</p>
 
  <hr>
 
  <h2>📋 Problem Statement</h2>
  <p>Accept a temperature value and its unit as input, then output the equivalent values in all three temperature units.</p>
 
  <hr>
 
  <h2>💡 Concepts Used</h2>
  <div class="concept-grid">
    <div class="concept-card"><span>Functions</span>One per conversion pair</div>
    <div class="concept-card"><span>User Input</span>input() + type casting</div>
    <div class="concept-card"><span>Conditionals</span>if / elif branching</div>
    <div class="concept-card"><span>Formatting</span>f-strings + :.2f</div>
  </div>
 
  <hr>
 
  <h2>🚀 How to Run</h2>
  <div class="run-box">
    <div>
      <div class="run-label">Terminal</div>
      <code>python temperature_converter.py</code>
    </div>
  </div>
 
  <hr>
 
  <h2>📥 Sample Input / Output</h2>
  <div class="io-grid">
    <div class="io-box">
      <div class="io-label">📥 Input</div>
      <pre><code>Enter Temperature Value: 100
Enter Unit (C/F/K): C</code></pre>
    </div>
    <div class="io-box">
      <div class="io-label">📤 Output</div>
      <pre><code>Celsius   : 100.00 °C
Fahrenheit: 212.00 °F
Kelvin    : 373.15 K</code></pre>
    </div>
  </div>
 
  <hr>
 
  <h2>🧮 Formulas Used</h2>
  <table>
    <tr><th>Conversion</th><th>Formula</th></tr>
    <tr><td>Celsius → Fahrenheit</td><td><code>(C × 9/5) + 32</code></td></tr>
    <tr><td>Celsius → Kelvin</td><td><code>C + 273.15</code></td></tr>
    <tr><td>Fahrenheit → Celsius</td><td><code>(F − 32) × 5/9</code></td></tr>
    <tr><td>Fahrenheit → Kelvin</td><td>Convert to °C first, then to K</td></tr>
    <tr><td>Kelvin → Celsius</td><td><code>K − 273.15</code></td></tr>
    <tr><td>Kelvin → Fahrenheit</td><td>Convert to °C first, then to °F</td></tr>
  </table>
 
  <hr>
 
  <h2>🧪 Test Cases</h2>
  <table>
    <tr><th>Input</th><th>Unit</th><th>Celsius</th><th>Fahrenheit</th><th>Kelvin</th></tr>
    <tr><td>100</td><td>C</td><td class="test-pass">100.00</td><td class="test-pass">212.00</td><td class="test-pass">373.15</td></tr>
    <tr><td>32</td><td>F</td><td class="test-pass">0.00</td><td class="test-pass">32.00</td><td class="test-pass">273.15</td></tr>
    <tr><td>0</td><td>K</td><td class="test-pass">−273.15</td><td class="test-pass">−459.67</td><td class="test-pass">0.00</td></tr>
  </table>
 
  <hr>
  <div class="footer">
    Part of <a href="https://github.com/your-username/python-fundamentals-practice">python-fundamentals-practice</a> —
    solved as part of Python Fundamentals practice before moving into Python Data Science.
  </div>
 
</div>
</body>
</html>
