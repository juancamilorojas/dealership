# Dealership - Vehicle Inheritance Project

This Python project demonstrates object-oriented programming concepts such as **inheritance**, **encapsulation**, and **polymorphism** using a base abstract class `Vehicle` and three subclasses: `Car`, `Motorcycle`, and `Plane`. Each subclass implements unique behaviors and characteristics.

## 🚗 Features

- **Inheritance:**
  - A base abstract class `Vehicle` defines common properties and methods.
  - Subclasses (`Car`, `Motorcycle`, `Plane`) inherit from `Vehicle` and implement additional specific behaviors.

- **Encapsulation:**
  - Sensitive attributes (e.g., password) are managed as private.

- **Polymorphism:**
  - Each subclass implements the `start()` and `move()` methods with distinct behaviors.

- **Abstraction:**
  - The `Vehicle` class is abstract and enforces subclasses to implement essential methods (`start` and `move`).

## 📂 Project Structure

```
dealership/
├── Vehicle.py
├── Car.py
├── Motorcycle.py
├── Plane.py
├── main.py
└── README.md
```

- **Vehicle.py:** Defines the abstract class `Vehicle`.
- **Car.py, Motorcycle.py, Plane.py:** Subclasses inheriting from `Vehicle`.
- **main.py:** Script for testing the classes by creating objects and demonstrating their behavior.

## ⚙️ Requirements

- Python 3.x
- No external libraries needed (uses Python standard library).

## 🚀 How to Run

Clone the repository:

```bash
git clone <your_repository_url>
cd dealership
```

Run the main script:

```bash
python main.py
```

The script will create instances of each vehicle, demonstrate their unique behaviors, and output the results in the terminal.

## 🛠️ Good Practices

- **Encapsulation:** Sensitive attributes (e.g., passwords) are managed using private attributes and getter/setter methods.
- **Polymorphism:** Demonstrated through unique implementations of methods like `move()` and `start()` in each subclass.

## 🎯 Future Improvements

- Add more vehicle types with unique behaviors.
- Enhance validation and error handling.
- Implement a graphical interface or integrate with a web application.

## 👤 Author

**Your Name Here**

- GitHub: [Your GitHub Profile](https://github.com/your_username)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

