#!/usr/bin/env python3
"""
Write a function named index_range that takes two integer arguments
page and page_size.
"""


def index_range(page, page_size):
    """Function index_range returns size two tuple containing
    start index and end index corresponding to range of indices
    to return a list of pagination parameters"""
    index_start = (page - 1) * page_size
    index_end = index_start + page_size
    return index_start, index_end
