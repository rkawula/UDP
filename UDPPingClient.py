from socket import *
from time import time

server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1) # 1 second timeout.

print "Attempting to connect to port %d:" %server_port

for i in range(10):
  message = "Sending ping %d" %(i + 1) # Number pings 1 through 10, inclusive.
  send_time = time()
  client_socket.sendto(message, (server_name, server_port))
  try:
    server_response, server_address = client_socket.recvfrom(2048)
    received_time = time()
    print "Server response received for: " + server_response
    print "RTT: %d" %(send_time - received_time) # Get time difference from send to receive.
  # timeout exception thrown when we reach the 1 second timeout threshold.
  except timeout:
  	print "Request timed out."

# Release socket for other programs.
client_socket.close()