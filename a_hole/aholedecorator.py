#!/usr/bin/env python3
"""Define the ``a_hole`` decorator."""

########################################################################################
# Silly decorators #1: @a_hole decorator
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
#
#
# (I mean, this is designed to deliberately break your code. Obviously, it has no
# warranty! I mean, c'mon!)
########################################################################################

from functools import wraps
from random import choice, random
from typing import Callable, Final, List

_MESSAGES: Final[List[str]] = [
    "AITA? Probably!",
    "Here's an exception to show you how much I care (about ruining your day).",
    "Perahps you should TRY catching these. (Get it, ha ha!)",
    "This is the exception that proves the rule--that this decorator sucks!",
    (
        "Whoever wrote me wasn't lying when they said 'WITHOUT WARRANTY OF ANY KIND"
        + ", EXPRESS OR IMPLIED'."
    ),
    (
        "I'm like a pâtissier, except I decorate functions instead of cakes, and I "
        + "decorate with U+1F4A9 instead of frosting."
    ),
]


class AHoleError(RuntimeError):
    """An exception to raise out of spite."""

    pass


def a_hole(func: Callable) -> Callable:
    """Make a function crash randomly."""

    @wraps(func)
    def new_func(*args, **kwargs):
        if random() <= 0.5:
            raise AHoleError(choice(_MESSAGES))
        else:
            return func(*args, **kwargs)

    return new_func


@a_hole
def example(x: float = 0.2) -> float:
    """Add a random number to the input."""
    return x + random()


if __name__ == "__main__":
    print(f"The output is {example():0.4f}.")
