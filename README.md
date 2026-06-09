<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Temperature Converter — README</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; background: #0d1117; color: #e6edf3; line-height: 1.7; padding: 40px 20px; }
    .container { max-width: 860px; margin: 0 auto; }
 
    h1 { font-size: 28px; font-weight: 600; border-bottom: 1px solid #30363d; padding-bottom: 12px; margin-bottom: 20px; color: #e6edf3; }
    h2 { font-size: 18px; font-weight: 600; border-bottom: 1px solid #30363d; padding-bottom: 8px; margin: 32px 0 14px; color: #e6edf3; }
 
    p { font-size: 15px; color: #8b949e; margin-bottom: 12px; }
 
    hr { border: none; border-top: 1px solid #30363d; margin: 28px 0; }
 
    .badge-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 20px; }
    .badge { padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500; }
    .b-blue  { background: #1f3a5f; color: #79c0ff; }
    .b-green { background: #1a3a2a; color: #56d364; }
    .b-amber { background: #3a2a10; color: #e3b341; }
    .b-gray  { background: #21262d; color: #8b949e; }
 
    pre { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; font-size: 13px; overflow-x: auto; margin-bottom: 16px; }
    code { font-family: 'Courier New', monospace; color: #e6edf3; }
    p code, li code { background: #161b22; padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #79c0ff; font-family: 'Courier New', monospace; }
 
    .concept-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; margin-bottom: 16px; }
    .concept-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 10px 14px; font-size: 13px; color: #8b949e; }
    .concept-card span { display: block; font-weight: 600; color: #e6edf3; margin-bottom: 2px; font-size: 14px; }
 
    table { width: 100%; border-collapse: collapse; font-size: 14px; margin-bottom: 16px; }
    th { background: #161b22; color: #8b949e; font-weight: 600; text-align: left; padding: 10px 14px; border: 1px solid #30363d; }
    td { padding: 9px 14px; border: 1px solid #30363d; color: #e6edf3; }
    tr:nth-child(even) td { background: #161b22; }
    td code { color: #79c0ff; }
 
    .test-pass { color: #56d364; font-weight: 600; }
    .footer { margin-top: 40px; padding-top: 16px; border-top: 1px solid #30363d; font-size: 13px; color: #8b949e; }
    .footer a { color: #79c0ff; text-decoration: none; }
    .footer a:hover { text-decoration: underline; }
 
    .run-box { display: flex; align-items: center; gap: 12px; background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 14px 18px; margin-bottom: 16px; }
    .run-box code { font-size: 14px; color: #56d364; }
    .run-label { font-size: 12px; color: #8b949e; }
 
    .io-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-bottom: 16px; }
    @media(max-width:560px){ .io-grid { grid-template-columns: 1fr; } }
    .io-box { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 14px; }
    .io-box .io-label { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; color: #8b949e; margin-bottom: 8px; }
  </style>
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
 
  <h2>📂 Repository Structure</h2>
  <pre><code>python-fundamentals-practice/
└── 01_variables_input/
    ├── temperature_converter.py
    └── README.html</code></pre>
 
  <div class="footer">
    Part of <a href="https://github.com/your-username/python-fundamentals-practice">python-fundamentals-practice</a> —
    solved as part of Python Fundamentals practice before moving into Python Data Science.
  </div>
 
</div>
</body>
</html>
