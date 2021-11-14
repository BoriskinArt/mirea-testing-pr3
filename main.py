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


def main():



if __name__ == "__main__":
    main()
