#!/usr/bin/env python3
'''get data on specific page'''
import csv
import math
from typing import Tuple, List, Dict


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
        '''initalizer of server object'''
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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''retrieves a info about a page
        '''
        assert type(page) == int and page > 0
        assert type(page_size) == int and page_size > 0
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_page': total_pages,
        }
        return page_info
