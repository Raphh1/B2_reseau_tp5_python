import socket
import struct

def send_message(sock, message):
    # Calculate the size of the message
    message_size = len(message)

    # Create a header with the message size
    header = struct.pack('!I', message_size)

    # Send the header, the message, and the ending sequence
    sock.send(header + message.encode() + "A".encode())

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))

# Send a 'Hello' message
send_message(s, 'Hello')

# Receive and print the response
data = s.recv(1024)
print(data.decode())

# Get a mathematical expression from the user
expression = input("Enter a mathematical expression (e.g., 3 + 3): ")

# Validate and send the expression
# You may want to add more robust validation here
if len(expression) <= 256:  # Assuming a reasonable maximum length for the expression
    send_message(s, expression)
else:
    print("Invalid expression length. Must be less than or equal to 256 characters.")

# Receive and print the result
result = s.recv(1024)
print(result.decode())

# Close the connection
s.close()
