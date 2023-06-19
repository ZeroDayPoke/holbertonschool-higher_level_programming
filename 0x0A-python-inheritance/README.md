# 0x0A. Python - Inheritance

This project is part of the Holberton School curriculum. In this project, you will learn about Python inheritance, how to use it, and how to create classes that inherit from other classes.

## Synopsis

This project covers:

- What is a superclass, baseclass or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- What is the purpose of inheritance
- What are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions

## File Descriptions

### Mandatory

- `0-lookup.py`: A function that returns the list of available attributes and methods of an object. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py)

- `1-my_list.py`: A class `MyList` that inherits from `list`. There is a public instance method `print_sorted` that prints the list, but sorted (ascending sort). [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py)

- `2-is_same_class.py`: A function that returns `True` if the object is exactly an instance of the specified class; otherwise `False`. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py)

- `3-is_kind_of_class.py`: A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py)

- `4-inherits_from.py`: A function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py)

- `5-base_geometry.py`: An empty class `BaseGeometry`. [Link tofile](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py)

- `6-base_geometry.py`: A class `BaseGeometry` (based on `5-base_geometry.py`). There is a public instance method `area` that raises an `Exception` with the message `area() is not implemented`. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py)

- `7-base_geometry.py`: A class `BaseGeometry` (based on `6-base_geometry.py`). There is a public instance method `integer_validator` that validates values. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py)

- `8-rectangle.py`: A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/8-rectangle.py)

- `9-rectangle.py`: A class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). There is a method `area` implemented. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py)

- `10-square.py`: A class `Square` that inherits from `Rectangle` (`9-rectangle.py`). [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/10-square.py)

- `11-square.py`: A class `Square` that inherits from `Rectangle` (`9-rectangle.py`). There is a method `__str__` implemented. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/11-square.py)

### Advanced

- `100-my_int.py`: This script contains the MyInt class which inherits from the int class. It overrides the == and != operators. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/100-my_int.py)

- `101-add_attribute.py`: This script contains a function add_attribute that adds a new attribute to an object if it's possible. [Link to file](https://github.com/ZeroDayPoke/holbertonschool-higher_level_programming/blob/master/0x0A-python-inheritance/101-add_attribute.py)

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
