#!/usr/bin/env python3
"""
Write a type-annotated function sum_mixed_list
which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""
from typing import List


def sum_mixed_list(mxd_list: List[int or float]) -> float:
    """ sum_mixed_list function declaration"""
    return sum(mxd_list)
