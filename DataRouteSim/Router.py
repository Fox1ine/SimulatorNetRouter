class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}

    def link(self, server):
        print(f"Server with IP {server.ip} connected.")
        self.servers[server.ip] = server
        server.router = self

    def unlink(self, server):
        if server is self.servers[server.ip]:
            print(f"Server with IP {server.ip} disconnected.")
            del self.servers[server.ip]
            server.router = None

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
                print(f"Router forwarding data to IP {data.ip}: '{data.data}'")
        self.buffer.clear()