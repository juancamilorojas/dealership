from Car import Car
from Motorcycle import Motorcycle
from Plane import Plane

def main():
    print("=== Vehicle Test ===\n")
    
    # Create and test Car object
    car = Car("Red", "Toyota", max_velocity=180, password='1234')
    car.start('1234')
    car.move()
    print(Car)
    print()
    
    # Create and test Motorcycle object
    motorcycle = Motorcycle("Blue", "Suzuki", max_velocity=180, password='1234')
    motorcycle.start('1234')
    motorcycle.move()
    print(motorcycle)
    print()
    
    # Create and test Plane object
    plane = Plane(color="white", brand="Boeing", max_velocity=900)
    # Intento de encendido sin checklist
    plane.start()
    # Realizar checklist, encender y mover el avión
    plane.do_checklist()
    plane.start()
    plane.move()
    print(plane)
    
if __name__ == '__main__':
    main()
