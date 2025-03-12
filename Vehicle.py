from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, color, brand, max_velocity, gas_level=100):
        self.color = color
        self.brand = brand 
        self.velocity = 0
        self.gas_level = gas_level
        self.on = False
        self.max_velocity = max_velocity
    
    def get_gas_level(self):
        return self.gas_level
    
    def get_velocity(self):
        return self.velocity

    def refuel(self, magnitude):
        max_fuel_level= (100 - self.get_gas_level() - magnitude) > 0
        if self.on & (self.gas_level < 100) & (self.velocity ==0) & (max_fuel_level):
            self.gas_level +=magnitude
            self.get_gas_level()

    def acelerate(self, magnitude):
        max_velocity_check= (self.max_velocity - self.get_velocity() - magnitude)>0
        if self.on & (self.gas_level >= 5) & (max_velocity_check) & (magnitude <=50):
            self.velocidad +=magnitude
            self.nivel_combustible -=5
            print('The vehicule is Acelerating')
        else:
            print('Is not possible to acelerate')
    
    @abstractmethod
    
    def start(self):
        """Each vehicle starts different"""
        pass
    
    @abstractmethod

    def move(self):
        """Each vehicle moves different"""
        pass

    def __str__(self):
        return (f"{self.__class__.__name__} [Color: {self.color}, Brand: {self.brand}, "
                f"Velocity: {self.velocity} km/h, Gas Level: {self.gas_level}%]")



