class Data:
    def __init__(self, a: float):
        if a > 0:
            self.a = a
        else:
            self.a = 0

    # km
    def convert_km_to_m(self):
        return self.a * (10 ** 3)

    def convert_km_to_dm(self):
        return self.a * (10 ** 2)

    def convert_km_to_cm(self):
        return self.a * (10 ** 5)

    def convert_km_to_mm(self):
        return self.a * (10 ** 6)

    # m
    def convert_m_to_km(self):
        return self.a * (10 ** -3)

    def convert_m_to_dm(self):
        return self.a * (10 ** 1)

    def convert_m_to_cm(self):
        return self.a * (10 ** 2)

    def convert_m_to_mm(self):
        return self.a * (10 ** 3)

    # dm
    def convert_dm_to_km(self):
        return self.a * (10 ** -4)

    def convert_dm_to_m(self):
        return self.a * (10 ** -1)

    def convert_dm_to_cm(self):
        return self.a * (10 ** 1)

    def convert_dm_to_mm(self):
        return self.a * (10 ** 2)

        # cm
    def convert_cm_to_km(self):
        return self.a * (10 ** -5)

    def convert_cm_to_m(self):
        return self.a * (10 ** -2)

    def convert_cm_to_dm(self):
        return self.a * (10 ** -1)

    def convert_cm_to_mm(self):
        return self.a * (10 ** 1)

    # mm
    def convert_mm_to_km(self):
        return self.a * (10 ** -6)

    def convert_mm_to_m(self):
        return self.a * (10 ** -3)

    def convert_mm_to_dm(self):
        return self.a * (10 ** -2)

    def convert_mm_to_cm(self):
        return self.a * (10 ** -1)

    # Miles
    def convert_miles_to_km(self):
        return self.a * 1.61

    def convert_miles_to_m(self):
        return self.a * 1609.34

    def convert_miles_to_dm(self):
        return self.a * 16093.4

    def convert_miles_to_cm(self):
        return self.a * 160934

    def convert_miles_to_mm(self):
        return self.a * 1609340

    # inch
    def convert_inch_to_km(self):
        return self.a * 0.000025

    def convert_inch_to_m(self):
        return self.a * 0.025

    def convert_inch_to_dm(self):
        return self.a * 0.25

    def convert_inch_to_cm(self):
        return self.a * 2.54

    def convert_inch_to_mm(self):
        return self.a * 25.4

    # ft
    def convert_ft_to_km(self):
        return self.a * 0.0003

    def convert_ft_to_m(self):
        return self.a * 0.3

    def convert_ft_to_dm(self):
        return self.a * 3.05

    def convert_ft_to_cm(self):
        return self.a * 30.48

    def convert_ft_to_mm(self):
        return self.a * 304.8


def main():
    while True:
        print("Выберете изначальную величину\n1 - километры\n2 - метры\n3 - дециметры\n4 - сантиметры\n"
              "5 - миллиметры\n6 - мили\n7 - футы\n")
        i = int(input())

        data = Data(float(input("Значение: ")))

        if i == 1:
            print("В метрах:", data.convert_km_to_m())
            print("В дециметрах:", data.convert_km_to_dm())
            print("В сантиметрах:", data.convert_km_to_cm())
            print("В миллиметрах:", data.convert_km_to_mm())

        elif i == 2:
            print("В километрах:", data.convert_m_to_km())
            print("В дециметрах:", data.convert_m_to_dm())
            print("В сантиметрах:", data.convert_m_to_cm())
            print("В миллиметрах:", data.convert_m_to_mm())

        elif i == 3:
            print("В километрах:", data.convert_dm_to_km())
            print("В метрах:", data.convert_dm_to_m())
            print("В сантиметрах:", data.convert_dm_to_cm())
            print("В миллиметрах:", data.convert_dm_to_mm())

        elif i == 4:
            print("В километрах:", data.convert_cm_to_km())
            print("В метрах:", data.convert_cm_to_m())
            print("В дециметрах:", data.convert_cm_to_dm())
            print("В миллиметрах:", data.convert_cm_to_mm())

        elif i == 5:
            print("В километрах:", data.convert_mm_to_km())
            print("В метрах:", data.convert_mm_to_m())
            print("В дециметрах:", data.convert_mm_to_dm())
            print("В сантиметрах:", data.convert_mm_to_cm())

        elif i == 6:
            print("В километрах:", data.convert_miles_to_km())
            print("В метрах:", data.convert_miles_to_m())
            print("В дециметрах:", data.convert_miles_to_dm())
            print("В сантиметрах:", data.convert_miles_to_cm())
            print("В миллиметрах:", data.convert_miles_to_mm())

        elif i == 7:
            print("В километрах:", data.convert_ft_to_km())
            print("В метрах:", data.convert_ft_to_m())
            print("В дециметрах:", data.convert_ft_to_dm())
            print("В сантиметрах:", data.convert_ft_to_cm())
            print("В миллиметрах:", data.convert_ft_to_mm())


if __name__ == "__main__":
    main()
