class Car:
    weight = 0
    height = 0
    def __init__(self,color="black",kind ="car",power=300, celinders=33, volume=1):
        self.color = color
        self.kind = kind
        self.power = power
        self.celinders = celinders
        self.volume = volume

    def update_weight_class(self, value):
        self.weight = value
    def update_height_class(self, value):
        self.height = value

#toyota: Car = Car()
#jeep: Car = Car()
#toyota.update_weight_class(123)
#jeep.update_weight_class(234)
#toyota.update_height_class(444)
#toyota.update_height_class()
#jeep.update_height_class()

    @classmethod
    def update_weight_class(cls, value):
        cls.weight = 0
    @staticmethod
    def car_signal():
        return ("beep-beep")
    @property
    def my_power(self):
        return self.celinders * self.volume
    def set_power(self, value):
        self.power
    def del_power(self):
        del self.power

toyota = Car()
jeep = Car()




#print(Car.update_weight_class(222))




#__call__(self, action="turn on")
#car1 = Car()
#print(Car())





#def __repr__(self):
#    return f"{self.name}"
#
#def update_weight_class(self, value):
#    self.weight =