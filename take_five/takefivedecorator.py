#!/usr/bin/env python3
"""Define the ``take_five`` decorator."""

########################################################################################
# Silly decorators #3: @take_five decorator
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
from datetime import datetime, timedelta
from functools import wraps
from random import choice
from typing import Final

TAKE_FIVE_GLYPHS: Final[list[str]] = [
    "\U0001f3b5",  # musical note
    "\U0001f3b6",  # musical notes
    "\U0001f3b7",  # saxophone
    "\U0001f3b8",  # guitar (for bass)
    "\U0001f3b9",  # musical keyboard
    "\U0001f3bc",  # musical score
    "\U0001f941",  # drum
]

NUM_TIME_DIVISIONS: Final[int] = 12


def take_five(func: Callable) -> Callable:
    """Add a bit of jazz to your ``Callable``."""

    @wraps(func)
    def returned_function(*args, **kwargs):
        end_times: list[datetime] = [
            datetime.now() + timedelta(milliseconds=(5000 * k) // NUM_TIME_DIVISIONS)
            for k in range(0, NUM_TIME_DIVISIONS + 1)
        ]
        returned_value = func(*args, **kwargs)
        jazz: str = ""
        for t in end_times:
            # Dut dut dodododo dut dut doooooo ...
            while datetime.now() < t:
                pass
            jazz += choice(TAKE_FIVE_GLYPHS)
            print(jazz + " \r", end="")
        print("")
        return returned_value

    return returned_function


if __name__ == "__main__":

    @take_five
    def my_add(a: int, b: int) -> int:
        """Add two integers."""
        return a + b

    print(my_add(2, 3))
