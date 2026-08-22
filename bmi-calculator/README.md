# BMI Calculator

A simple script that asks for someone's name, weight, and height, then calculates their Body Mass Index (BMI) and tells them which category they fall into, underweight, normal weight, overweight, obese, severely obese, or morbidly obese.

Nothing fancy here on purpose, this was about getting comfortable with taking user input, doing a real calculation with it, and then using conditional logic to turn a raw number into something meaningful and readable.

## How it works

1. Asks the user for their **name**, **weight (in pounds)**, and **height (in inches)**
2. Calculates BMI using the standard formula:

   ```
   BMI = (weight * 703) / (height * height)
   ```

3. Rounds the result to 2 decimal places
4. Runs the BMI through a series of `if` / `elif` checks to classify it into a category:
   - Below 18.5 → Underweight
   - 18.5 – 24.9 → Normal weight
   - 24.9 – 29.9 → Overweight
   - 29.9 – 34.9 → Obese
   - 34.9 – 39.9 → Severely obese
   - Above 39.9 → Morbidly obese
5. Prints a personalized message using the name and result
6. If the BMI comes out as zero or negative (meaning the inputs didn't make sense), it prints a message asking for accurate inputs instead of showing a broken result

## Why I built it this way

The interesting part isn't the formula, it's the layered `if`/`elif` chain that turns one number into a clear, human-readable category, plus the script doesn't confidently print nonsense if someone enters bad input.

## Tools used
- Python (built-in `input()`, arithmetic, conditional logic)
- Jupyter Notebook

## Files
- `bmi_calculator.ipynb` — the notebook version
- `bmi_calculator.py` — plain script version (recommended way to actually run this one)

## How to run it

```bash
python bmi_calculator.py
```
You'll be prompted to enter your name, weight, and height, and the result will print directly in the terminal.

## What I'd improve next
- Add support for metric units (kg/cm), not just imperial
- Handle non-numeric input gracefully instead of crashing on bad entries
- Turn it into a small function so it can be reused/tested rather than running top-to-bottom as a script

---
*Part of my Python Mini Projects collection.*
