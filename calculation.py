#!\usr\bin\env python3

import re
import os
import sys


def func_a():
    print("This is a function a")
    os.exit(1)

def func_b():
    print("This is a function b")
    os.exit(1)

func_a()
