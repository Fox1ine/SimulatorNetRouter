from DataRouteSim.Data import Data
from DataRouteSim.Server import Server
from DataRouteSim.Router import Router

# Create a router instance
router = Router()

# Create server instances
sv_from = Server()
sv_from2 = Server()
sv_to = Server()

# Link servers to the router
router.link(sv_from)
router.link(sv_from2)
router.link(sv_to)

# Servers send data to each other
sv_from.send_data(Data("Hello from Server 1", sv_to.get_ip()))
sv_from2.send_data(Data("Hello from Server 2", sv_to.get_ip()))
sv_to.send_data(Data("Hi back to Server 1", sv_from.get_ip()))

# Process the data in the router
router.send_data()

# Servers retrieve their messages
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

# Print out the messages each server received
print(f"Server {sv_from.get_ip()} received: {[data.data for data in msg_lst_from]}")
print(f"Server {sv_to.get_ip()} received: {[data.data for data in msg_lst_to]}")
