from .es import build_edge_servers_randomly

class MECEnv:
    def __init__(args):
        self.edge_servers = build_edge_servers_randomly(
            args.num_servers, 
            args.latitude_range,
            args.longtitude_range,
            args.bandwidth_range, 
            args.capacity_range
        )


