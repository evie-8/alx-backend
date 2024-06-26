#!/usr/bin/env python3
'''function to get info on a page'''
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''Computes index range'''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''Initializer of object'''
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
        """Retrieves data for a particular page"""
        assert type(page) == int and type(page_size) == int
        assert (page > 0 and page_size > 0)
        start, end = index_range(page, page_size)
        pageData = self.dataset()
        if start > len(pageData):
            return []
        return pageData[start:end]
