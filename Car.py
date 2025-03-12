from Vehicle import Vehicle
import random

class Car(Vehicle):
    def __init__(self, color, brand, max_velocity, password):
        super().__init__(color, brand, max_velocity, password)
        self.__password = password  # atributo privado
        self.gas_level=100

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password=new_password
    
    def start(self, password):
        if (self.__password == password):
            state=True
            print('Car is ON')
        else: 
            print('Incorrect password, check again')


    def move(self):
        if self.on & self.gas_level >= 5:
            self.velocidad +=10
            self.nivel_combustible -=2
            print('The car is moving on 4 weels, traveling on the highway')
        else: 
            print('is not possible to start the vehicule. Check that you started the engine and that the gas level is above 5%')



