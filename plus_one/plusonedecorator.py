#!/usr/bin/env python3
"""Define the ``plus_one`` decorator."""

########################################################################################
# Silly decorators #2: @plus_one decorator
#
# By Christopher Phan, cphan@chrisphan.com
# github: christopherphan
#
# MIT License
#
# Copyright (c) 2022 Christopher Phan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
########################################################################################

from collections.abc import Callable
from functools import wraps
from numbers import Complex
from typing import Union


def plus_one(func: Callable) -> Callable:
    """Decorate a function to make its output off by 1."""

    @wraps(func)
    def returned_function(*args, **kwargs) -> Union[Complex, str]:
        """Add one to the output of ``func``."""
        output = func(*args, **kwargs)
        if isinstance(output, Complex):
            return output + 1
        else:
            outstring = str(output)
            if outstring[-1] in [".", "?", "!", '"', "'", "\n", ",", ";"]:
                add_last = outstring[-1]
                outstring = outstring[:-1]
            else:
                add_last = ""
            return f"{outstring} plus one{add_last}"

    return returned_function


@plus_one
def example(x: float = 0.2) -> float:
    """Add one to the input."""
    return x


if __name__ == "__main__":
    print(f"The output is {example():0.4f}.")
