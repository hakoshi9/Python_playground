
class BodyCalculator():
    # 体重kg * (身長m)^2
    def bmi(self, user_weight=None, user_hegiht=None):
        """
        Calculates users bmi according to the users weight and height.

        Logic:
            BMI: weight(km) / height(m)^2

        Args:
            weight(float/int): Users weight. Default is set at None.
            hegiht(float/int): Users height. Default is set at None.

        Returns:
            bmi(float): Returns users bmi.
        """
        user_bmi = user_weight / user_hegiht ** 2  # users bmi
        bmi = round(user_bmi, 1)  # round it to .0
        return bmi


    def basal_metabolism(self, gender=None, weight=None, height=None, age=None):
        """
        Calculates users basal metabolism using the users gender, weight, height and age.

        Logic:
            Male: 66.47 + (13.75*W) + (5.00*H) - (6.78*A)
            Female: 655.1 + (9.56*W) + (1.85*H) - (4.68*A)
            W: weight(kg)  H: height(cm)  A: age

        Args:
            gender(int): Users gender. Default is set at None.
            weight(float/int): Users weight. Default is set at None.
            height(float/int): Users height. Default is set at None.
            age(int): Users age. Default is set at None.

        Returns:
            basal_metabolism(float): Returns users 
        """
        pass


    def suitable_weight(self):
        pass


    def ideal_absorb_calories(self):
        pass