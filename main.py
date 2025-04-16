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
    hoge = add(1, 2)
    print(f"Sum of 1 and 2 is: {hoge:04d}")


def add(a, b):
    """
    Function to add two numbers.
    :param a: First number
    :param b: Second number
    :return: Sum of a and b
    """
    return a + b


if __name__ == "__main__":
    main()