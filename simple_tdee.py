import argparse
import math

class Person:
    def __init__(self, gender, age, weight_kg=0, weight_lb=0, height_m=0, height_in=0, bmi=0, orig_hb_bmr=0):
        self.gender = gender
        self.age = age
        self.weight_kg = weight_kg
        self.weight_lb = weight_lb
        self.height_m = height_m
        self.height_in = height_in
        self.bmi = bmi
        self.orig_hb_bmr = orig_hb_bmr

    def convert_imp_to_metric(self):
        self.weight_kg = round(self.weight_lb / 2.205, 1)
        self.height_m = round(self.height_in / 39.37, 1)
        return self.weight_kg, self.height_m

    def calc_bmi(self):
        self.bmi = round(self.weight_kg / math.pow(self.height_m, 2), 1)
        return self.bmi

    def calc_orig_harris_benedict(self):
        """
            THIS FUNCTION CALCULATES THE ORIGINAL HARRIS-BENEDICT BMR EQUATION
            MEN - BMR = 66.4730 + (13.7516 x weight in kg) + (5.0033 x height in cm) – (6.7550 x age in years)
            WOMEN - BMR = 655.0955 + (9.5634 x weight in kg) + (1.8496 x height in cm) – (4.6756 x age in years)
        """
        if self.gender == "male":
            self.orig_hb_bmr = round(66.4730 + (13.7516 * self.weight_kg) + (5.0033 * (self.height_m * 100)) - (6.7550 * self.age), 1)

        if self.gender == "female":
            self.orig_hb_bmr = round(655.0955 + (9.5634 * self.weight_kg) + (1.8496 * (self.height_m * 100)) - (4.6756 * self.age), 1)

        return self.orig_hb_bmr


def main():
    parser = argparse.ArgumentParser(description="A Python Total Daily Energy Expenditure (TDEE) CLI Calculator. This program uses" +
                                                 "the Mifflin-St Jeor Equation to calculate TDEE as it's considered to be more accurate," +
                                                 "see https://www.ncbi.nlm.nih.gov/pubmed/15883556.")
    parser.add_argument("--unit", metavar="UNIT", help="Unit of Measurement", choices=["metric", "imperial"], dest="unit_arg", required=True)
    parser.add_argument("--weight", metavar="WEIGHT", type=float, help="Your Weight.", dest="weight_arg")
    parser.add_argument("--height", metavar="HEIGHT", type=float, help="Your Height.", dest="height_arg")
    parser.add_argument("--age", metavar="AGE", type=float, help="Your Age.", dest="age_arg")
    parser.add_argument("--gender", metavar="GENDER", help="Your Gender.", choices=["male", "female"], dest="gender_arg")
    args = parser.parse_args()
    print(args)
    gender_arg = args.gender_arg
    age_arg = args.age_arg
    unit_arg = args.unit_arg
    weight_arg = args.weight_arg
    height_arg = args.height_arg
    if unit_arg == "imperial":
        print("imperial")
        p = Person(gender=gender_arg,
                   age=age_arg,
                   weight_lb=weight_arg,
                   height_in=height_arg)
        p.weight_kg, p.height_m = p.convert_imp_to_metric()
        print(p.weight_kg, p.height_m)
        bmi = p.calc_bmi()
        print(bmi)
        x = p.calc_orig_harris_benedict()
        print(x)

    else:
        print("metric")


if __name__ == "__main__":
    main()