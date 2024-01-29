#!/usr/bin/env python3
""" An helper or wrapper"""

import csv
import math
from typing import List, Tuple, Dict


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
            """A method that finds correct index_range to return"""
            assert isinstance(page, int) and isinstance(page_size, int) and \
                    page > 0 and page_size > 0
            return_value = index_range(page, page_size)

            dataset = self.dataset()
            try:
                specified_reading = dataset[return_value[0]: return_value[1]]
                return specified_reading
            except IndexError:
                return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get hypermedia paging"""
        hypermedia = {}
        dataset = self.dataset()
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(dataset) / page_size)

        hypermedia["page_size"] = len(data)
        hypermedia["page"] = page
        hypermedia["data"] = data
        hypermedia["next_page"] = page + 1 if page < total_pages else None
        hypermedia["previous_page"] = page - 1 if page > 1 else None
        hypermedia["total_pages"] = total_pages

        return hypermedia


def index_range(page: int, page_size: int) -> Tuple:
    """ A function that creates a range of
       page to be returned by a query
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    tuple_of_range = (start_index, end_index)

    return tuple_of_range
