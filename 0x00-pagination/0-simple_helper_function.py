#!/usr/bin/env python3
'''
Module that returns the starting index  and ending index
'''
from typing import Tuple


def index_range(page: int, page_size:int) -> Tuple[int, int]:
    '''
    Computes index range
    '''
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
