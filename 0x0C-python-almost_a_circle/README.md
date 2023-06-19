# 0x0C - Almost A Circle

This project is a collection of classes that represent shapes like rectangles and squares, and their tests. The classes are located in the `models/` directory and the tests are in the `tests/` directory.

## Models

The `models/` directory contains the following files:

1. `base.py`: This file contains the `Base` class which is the base class for other classes in this project. It manages the id attribute for all instances.

2. `rectangle.py`: This file contains the `Rectangle` class which inherits from `Base`. It represents a rectangle and manages the width, height, x, and y attributes. It also includes methods for area calculation, display, and conversion to dictionary.

3. `square.py`: This file contains the `Square` class which inherits from `Rectangle`. It represents a square and manages the size attribute.

## Tests

The `tests/` directory contains the following files:

1. `test_models/test_base.py`: This file contains the unit tests for the `Base` class. It tests for id incrementation and JSON string representation and file saving/loading.

2. `test_models/test_rectangle.py`: This file contains the unit tests for the `Rectangle` class. It tests for attribute validation and getter/setter functionality, area calculation, display, dictionary conversion, and JSON string representation.

3. `test_models/test_square.py`: This file contains the unit tests for the `Square` class. It tests for attribute validation and getter/setter functionality, area calculation, display, dictionary conversion, and JSON string representation.

Please refer to the individual files for more detailed information about each class and their methods.

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
