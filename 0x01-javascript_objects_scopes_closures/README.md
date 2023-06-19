# 0x01. JavaScript - Objects, Scopes and Closures

This project is part of the Holberton School curriculum. In this project, you will learn about JavaScript objects, scopes, and closures.

## Synopsis

This project covers:

- How to create an object in JavaScript
- What `this` means
- What `undefined` means
- Why the variable type and scope is important
- What is a closure
- What is a prototype
- How to inherit an object from another

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 14.04 LTS using `node` (version 10.14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
- All your files must be executable
- The length of your files will be tested using `wc`

## File Descriptions

- `0-rectangle.js`: This JavaScript script defines an empty class `Rectangle`.
- `1-rectangle.js`: This JavaScript script defines a class `Rectangle` that takes in 2 arguments `w` and `h`.
- `2-rectangle.js`: This JavaScript script defines a class `Rectangle` that takes in 2 arguments `w` and `h`. The `Rectangle` class is defined with a width and a height. The width and height are set to 0 if they are less than or equal to 0.
- `3-rectangle.js`: This JavaScript script defines a class `Rectangle` that defines a rectangle. If `w` or `h` is equal to 0 or not a positive integer, create an empty object.
- `4-rectangle.js`: This JavaScript script defines a class `Rectangle` that defines a rectangle. The `Rectangle` class now includes a `rotate()` method that exchanges the `width` and the `height` of the rectangle and a `double()` method that multiples the `width` and the `height` of the rectangle by 2.
- `5-square.js`: This JavaScript script defines a class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`.
- `6-square.js`: This JavaScript script defines a class `Square` that defines a square and inherits from `Square` of `5-square.js`.
- `7-occurrences.js`: This JavaScript script returns the number of occurrences in a list.
- `8-esrever.js`: This JavaScript script returns the reversed version of a list.
- `9-logme.js`: This JavaScript script prints the number of arguments already printed and the new argument value.
- `10-converter.js`: This JavaScript script converts a number from base 10 to another base passed as argument.

## Author

Chris Stamper - [ZeroDayPoke](https://github.com/ZeroDayPoke)
