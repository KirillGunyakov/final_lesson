from datetime import datetime
class Data:

        def __init__(self, str):
            self.str = str

        def __str__(self):
            return str(self.str)

        @classmethod
        def to_int(cls, str):
            dline = datetime.strptime(str, "%d-%m-%Y")
            d = dline.day
            m = dline.month
            y = dline.year
            cls.d = d
            cls.m = m
            cls.y = y
            return d, m, y

        @staticmethod
        def to_valid(param1, param2, param3):
            if (param1 in range(1, 31)) and (param2 in range(1, 12)):
                return True
            else:
                return False


s = "02-11-2021"
dat = Data(s)

print(dat)
print(dat.to_int(s))
print(dat.d)

x, y, z = dat.to_int(s)
print('данные ', x, y, z)
print(dat.to_valid(x, y, z))
