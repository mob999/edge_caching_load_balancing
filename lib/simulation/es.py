from typing import Tuple
from lib.util import random_utils
import random
random_utils.set_seed()

class EdgeServer:
    def __init__(
        position: Tuple[int, int], 
        max_bandwidth: int, 
        max_capacity: int
        ):
        self.position = position
        self.max_bandwidth = max_bandwidth
        self.max_capacity = max_capacity

def build_edge_servers_randomly(
    num_servers: int, 
    latitude_range: Tuple[int, int], 
    longtitude_range: Tuple[int, int],
    bandwidth_range: Tuple[int, int], 
    capacity_range: Tuple[int, int]
    ):
    return [
        EdgeServer(
            (_from_range_get_int(latitude_range), _from_range_get_int(longtitude_range)),
            _from_range_get_int(bandwidth_range),
            _from_range_get_int(capacity_range)
        ) for _ in range(num_servers)
    ]

def _from_range_get_int(_range: Tuple[int, int]):
    return random.randint(_range[0], _range[1])