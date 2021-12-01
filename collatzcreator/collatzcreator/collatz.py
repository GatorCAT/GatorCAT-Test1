"""Compute values in the Collatz sequence using an iterative approach."""

from typing import Iterator


def compute_collatz_chain(number: int) -> Iterator[int]:
    """Perform collatz chain on given number."""
    # yield the original input number
    # continue to iterate until the number is equal to 1
    # NOTE: there is no proof that this function will stop running!
    # NOTE: can you provide an answer to the following problem?
    # Add in all of the remaining functionality for this function
    # Reference:
    # https://projecteuler.net/problem=14
    yield number
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = 3 * number + 1
        yield number
