#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Uyu TANAKA
Date: 2023-10-01
Version: 1.0.0
License: MIT License
Description: Testing VSCode and Git.
Conda Environment: <your-conda-environment-name>
"""

def main():
    """
    Main function to execute the script.
    """
    print("Hello, VSCode and Git!")
    hoge = add_10(100, 200)
    print(f"Sum of 100 and 200 is: {hoge:04d}")


def add_10(a, b):
    """
    Function to add two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b + 10


if __name__ == "__main__":
    main()