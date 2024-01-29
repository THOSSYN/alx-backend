#!/usr/bin/env python3
""" An helper or wrapper"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """ A function that creates a range of
       page to be returned by a query
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tuple_of_range = (start_index, end_index)

    return tuple_of_range
