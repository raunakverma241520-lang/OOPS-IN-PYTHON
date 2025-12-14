# Object Oriented Programming (OOPS) in Python 🐍

## 📌 Introduction
Object Oriented Programming (OOPS) is a programming paradigm based on the concept of **objects**, which contain **data (attributes)** and **methods (functions)**.  
Python fully supports OOPS concepts, making code **reusable, modular, and easy to maintain**.

---

## 🧱 Core OOPS Concepts

### 1️⃣ Class
A **class** is a blueprint for creating objects.

```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
2️⃣ Object
An object is an instance of a class.

python
Copy code
s1 = Student("Amit", 101)
print(s1.name)
3️⃣ Encapsulation
Encapsulation means binding data and methods together and restricting direct access.

python
Copy code
class Account:
    def __init__(self):
        self.__balance = 0   # private variable

    def deposit(self, amount):
        self.__balance += amount
4️⃣ Inheritance
Inheritance allows a class to acquire properties of another class.

python
Copy code
class Person:
    def show(self):
        print("This is a person")

class Student(Person):
    pass
5️⃣ Polymorphism
Polymorphism allows methods to have the same name but different behavior.

python
Copy code
class Bird:
    def sound(self):
        print("Bird sound")

class Dog:
    def sound(self):
        print("Bark")

for obj in (Bird(), Dog()):
    obj.sound()
6️⃣ Abstraction
Abstraction hides implementation details and shows only essential features.

python
Copy code
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
🔑 Special Methods (Magic Methods)
Method	Description
__init__	Constructor
__str__	String representation
__del__	Destructor

python
Copy code
class Demo:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")
📂 Project Structure
powershell
Copy code
OOPS-in-Python/
│── class_object.py
│── inheritance.py
│── polymorphism.py
│── encapsulation.py
│── abstraction.py
└── README.md
🎯 Advantages of OOPS
Code reusability

Easy maintenance

Better security

Real-world modeling

Modular approach

🚀 How to Run
bash
Copy code
python filename.py
📚 Learning Resources
Python Official Docs: https://docs.python.org

W3Schools Python OOPS

GeeksforGeeks Python OOPS

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first.

