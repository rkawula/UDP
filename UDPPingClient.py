from socket import *
from time import time

server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1) # 1 sec timeout

print "Attempting to connect to port %d:" %server_port

for i in range(10):
  message = "Sending ping %d" %(i + 1)
  send_time = time()
  client_socket.sendto(message, (server_name, server_port))
  try:
    server_response, server_address = client_socket.recvfrom(2048)
    received_time = time()
    print "Server response received for: " + server_response
    print "RTT: %d" %(send_time - received_time)
  except timeout:
  	print "Request timed out."

client_socket.close()