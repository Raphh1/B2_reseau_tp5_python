import socket
import struct

def send_message(sock, message):

    message_size = len(message)


    header = struct.pack('!I', message_size)

 
    sock.send(header + message + "0".encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))


send_message(s, 'Hello'.encode())


data = s.recv(1024)
print(data.decode())


expression = input("Enter a mathematical expression (e.g., 3 + 3): ")



if len(expression) <= 256:  
    send_message(s, expression.encode())
else:
    print("Invalid expression length. Must be less than or equal to 256 characters.")


result_header = s.recv(4)
result_size = struct.unpack('!I', result_header)[0]
result = s.recv(result_size)
print("Result:", struct.unpack('!i', result)[0])


s.close()
