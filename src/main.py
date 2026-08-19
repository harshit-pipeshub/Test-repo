#!/usr/bin/env python3
"""Simple Python entrypoint for the sample files.

Run: python3 src/main.py
"""
from utils import add


def main():
    print("Hello from Test-repo sample files")
    a, b = 2, 3
    print(f"{a} + {b} = {add(a, b)}")


if __name__ == '__main__':
    main()
