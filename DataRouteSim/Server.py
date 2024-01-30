class Server:
    IP = 0

    def __init__(self):
        self.ip = Server.IP
        Server.IP += 1
        self.buffer = []
        self.router = None

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)
            print(f"Server {self.ip} sent data '{data.data}'")

    def get_data(self):
        if self.router:
            self.router.send_data()
            data = self.buffer.copy()
            self.buffer.clear()
            print(f"Server {self.ip} received data: {[d.data for d in data]}")
            return data
        return []

    def get_ip(self):
        return self.ip
