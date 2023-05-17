#!/usr/bin/env python3
"""
Implement a method named get_page that takes two integer arguments
page with default value 1 and page_size with default value 10.
"""
import csv
import math
from typing import List


def index_range(page, page_size):
    """Function index_range returns size two tuple containing
    start index and end index corresponding to range of indices
    to return a list of pagination parameters"""
    index_start = (page - 1) * page_size
    index_end = index_start + page_size
    return index_start, index_end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """get_page method to paginate a database"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()

        index_start, index_end = index_range(page, page_size)

        if index_start >= len(dataset):
            return []

        return dataset[index_start:index_end]
