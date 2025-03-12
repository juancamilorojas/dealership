from Vehicle import Vehicle 

class Plane(Vehicle):
    def __init__(self, color, brand, max_velocity):
        super().__init__(color, brand, max_velocity)
        self.checklist=False
        self.gas_level=100

    def do_checklist(self):
        self.checklist=True
        print('Checklist ok, ready to fly')
    
    def start(self):
        if (self.checklist):
            print('plane is ON')
        else: 
            print('Checklist not OK. Plane not ready to start')

    def move(self):
        if self.on & self.gas_level >= 5:
            self.velocity +=10
            self.gas_level -=2
            print('The plane is moving flying on the sky')
        else: 
            print('is not possible to start the plane. Check that you started the engine and that the gas level is above 5%')

