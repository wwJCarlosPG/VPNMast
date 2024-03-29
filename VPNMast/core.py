class Body:
    def __init__(
        self,
        dest_ip: str,
        dest_port: int,
        data: str,
        user: str = None,
        password: str = None,
    ):
        self.dest_ip = dest_ip
        self.dest_port = dest_port
        self.data = data
        if user is not None and password is not None:
            self.password = password
            self.user = user

    @staticmethod
    def dict_to_body(dict):
        dest_ip = dict["dest_ip"]
        dest_port = dict["dest_port"]
        data = dict["data"]

        value = Body(dest_ip, dest_port, data)

        return value


class Address:
    def __init__(self, _ip: str, _port: int):
        self.ip = _ip
        self.port = _port
