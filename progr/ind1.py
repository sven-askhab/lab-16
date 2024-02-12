#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from closure_module import f
from closure_module import outer_function

if __name__ == "__main__":
    closure = outer_function(f)

    print(closure(3, 4))