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
 
    
 
 
def main():
 
 
 
if __name__ == "__main__":
    main()