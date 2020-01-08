# Simple Python TDEE Calculator
Gives BMI, BMR of most popular equations, TDEE & caloric target based on percent increase/decrease of goals.
## Help
```$xslt
$ .\simple_tdee.py -h

usage: simple_tdee.py [-h] --unit UNIT [--weight WEIGHT] [--height HEIGHT] [--age AGE] [--gender GENDER] [--activity-level ACTIVITY LEVEL]

A Python Total Daily Energy Expenditure (TDEE) CLI Calculator.

This program uses the Mifflin-St Jeor Equation to calculate TDEE as it's considered to be more accurate,see https://www.ncbi.nlm.nih.gov/pubmed/15883556.

optional arguments:
  -h, --help            show this help message and exit
  --unit UNIT           Unit of Measurement
  --weight WEIGHT       Your Weight.
  --height HEIGHT       Your Height.
  --age AGE             Your Age.
  --gender GENDER       Your Gender.
  --activity-level ACTIVITY LEVEL
                        1.2 for Sedentary (little or no exercise, desk job)
                        1.375 for Lightly Active (light exercise/activity 1-3 days/week)
                        1.55 for Moderately Active (moderate exercise/activity 6-7 days/week)
                        1.725  for Very Active (2-3 hours of hard exercise every day)
                        1.9 for Extremely Active (hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.)

```

## Example
```$xslt
$ .\simple_tdee.py --gender male --age 28 --unit imperial --weight 188.4 --height 71 --activity-level 1.375

Your BMI: 26.4
Original Harris-Benedict Equation: 1952.3 cals
Revised Harris-Benedict Equation: 1937.3 cals
Mifflin-St. Jeor Equation 1844.0 cals
Total Daily Energy Expenditure (TDEE): 2535.5 cals
```