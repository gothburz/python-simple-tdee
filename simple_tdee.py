import argparse
import math
from argparse import RawTextHelpFormatter


class Person:
    def __init__(
        self,
        gender,
        age,
        weight_kg=0,
        weight_lb=0,
        height_m=0,
        height_in=0,
        bmi=0,
        orig_hb_bmr=0,
        rev_hb_bmr=0,
        mj_bmr=0,
        tdee=0,
        activity_level=0,
    ):
        self.gender = gender
        self.age = age
        self.weight_kg = weight_kg
        self.weight_lb = weight_lb
        self.height_m = height_m
        self.height_in = height_in
        self.bmi = bmi
        self.orig_hb_bmr = orig_hb_bmr
        self.rev_hb_bmr = rev_hb_bmr
        self.mj_bmr = mj_bmr
        self.tdee = tdee
        self.activity_level = activity_level

    def convert_imp_to_metric(self):
        self.weight_kg = self.weight_lb / 2.205
        self.height_m = self.height_in / 39.37

        return self.weight_kg, self.height_m

    def calc_bmi(self):
        self.bmi = self.weight_kg / math.pow(self.height_m, 2)
        return self.bmi

    def calc_orig_harris_benedict_bmr(self):
        """
        THIS FUNCTION CALCULATES THE ORIGINAL HARRIS-BENEDICT BMR EQUATION
        MEN - BMR = 66.4730 + (13.7516 x weight in kg) + (5.0033 x height in cm) – (6.7550 x age in years)
        WOMEN - BMR = 655.0955 + (9.5634 x weight in kg) + (1.8496 x height in cm) – (4.6756 x age in years)
        :return: Original Harris-Benedict BMR Value
        """
        if self.gender == "male":
            self.orig_hb_bmr = (
                66.4730
                + (13.7516 * self.weight_kg)
                + (5.0033 * (self.height_m * 100))
                - (6.7550 * self.age)
            )

        if self.gender == "female":
            self.orig_hb_bmr = (
                655.0955
                + (9.5634 * self.weight_kg)
                + (1.8496 * (self.height_m * 100))
                - (4.6756 * self.age)
            )

        return self.orig_hb_bmr

    def calc_rev_harris_benedict_bmr(self):
        """
        THIS FUNCTION CALCULATES THE REVISED HARRIS-BENEDICT BMR EQUATION
        MEN - BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
        WOMEN - BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)
        :return: Revised Harris-Benedict BMR Value
        """
        if self.gender == "male":
            self.rev_hb_bmr = (
                88.362
                + (13.397 * self.weight_kg)
                + (4.799 * (self.height_m * 100))
                - (5.677 * self.age)
            )
        if self.gender == "female":
            self.rev_hb_bmr = (
                447.593
                + (9.247 * self.weight_kg)
                + (3.098 * (self.height_m * 100))
                - (4.330 * self.age)
            )

        return self.rev_hb_bmr

    def calc_mj_bmr(self):
        """
        THIS FUNCTION CALCULATES THE MIFFLIN-ST JEOR BMR EQUATION
        MEN - BMR (metric) = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
        WOMEN - BMR (metric) = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161
        :return: Mifflin-St Jeor BMR
        """
        if self.gender == "male":
            self.mj_bmr = (10 * self.weight_kg) + (
                6.25 * (self.height_m * 100) - (5 * self.age) + 5
            )
        if self.gender == "female":
            self.mj_bmr = (10 * self.weight_kg) + (
                6.25 * (self.height_m * 100) - (5 * self.age) + 5
            )

        return self.mj_bmr

    def calc_tdee(self):
        self.tdee = self.mj_bmr * float(self.activity_level)

        return self.tdee


def main():
    parser = argparse.ArgumentParser(
        description="A Python Total Daily Energy Expenditure (TDEE) CLI Calculator.\n\n"
        + "This program uses the Mifflin-St Jeor Equation to calculate TDEE as it's considered to be more accurate,"
        + "see https://www.ncbi.nlm.nih.gov/pubmed/15883556.",
        formatter_class=RawTextHelpFormatter,
    )
    parser.add_argument(
        "--unit",
        metavar="UNIT",
        help="Unit of Measurement",
        choices=["metric", "imperial"],
        dest="unit_arg",
        required=True,
    )
    parser.add_argument(
        "--weight", metavar="WEIGHT", type=float, help="Your Weight.", dest="weight_arg"
    )
    parser.add_argument(
        "--height", metavar="HEIGHT", type=float, help="Your Height.", dest="height_arg"
    )
    parser.add_argument(
        "--age", metavar="AGE", type=float, help="Your Age.", dest="age_arg"
    )
    parser.add_argument(
        "--gender",
        metavar="GENDER",
        help="Your Gender.",
        choices=["male", "female"],
        dest="gender_arg",
    )
    parser.add_argument(
        "--activity-level",
        metavar="ACTIVITY LEVEL",
        help="1.2 for Sedentary (little or no exercise, desk job)\n"
        + "1.375 for Lightly Active (light exercise/activity 1-3 days/week)\n"
        + "1.55 for Moderately Active (moderate exercise/activity 6-7 days/week)\n"
        + "1.725  for Very Active (2-3 hours of hard exercise every day)\n"
        + "1.9 for Extremely Active (hard exercise 2 or more times per day, or training for marathon, or triathlon, etc.)",
        choices=["1.2", "1.375", "1.55", "1.725", "1.9"],
    )
    args = parser.parse_args()
    gender_arg = args.gender_arg
    age_arg = args.age_arg
    unit_arg = args.unit_arg
    weight_arg = args.weight_arg
    height_arg = args.height_arg
    activity_level = args.activity_level
    if unit_arg == "imperial":
        p = Person(
            gender=gender_arg,
            age=age_arg,
            weight_lb=weight_arg,
            height_in=height_arg,
            activity_level=activity_level,
        )
        p.weight_kg, p.height_m = p.convert_imp_to_metric()
        bmi = p.calc_bmi()
        print(f"Your BMI: {bmi:.1f}")
        orig_hb_bmr = p.calc_orig_harris_benedict_bmr()
        print(f"Original Harris-Benedict Equation: {orig_hb_bmr:.1f} cals")
        rev_hb_bmr = p.calc_rev_harris_benedict_bmr()
        print(f"Revised Harris-Benedict Equation: {rev_hb_bmr:.1f} cals")
        mj_bmr = p.calc_mj_bmr()
        print(f"Mifflin-St. Jeor Equation {mj_bmr:.1f} cals")
        tdee = p.calc_tdee()
        print(f"Total Daily Energy Expenditure (TDEE): {tdee:.1f} cals")

    else:
        print("metric")


if __name__ == "__main__":
    main()
