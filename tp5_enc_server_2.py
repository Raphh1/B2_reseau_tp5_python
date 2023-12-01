import socket
import struct

def receive_message(conn):
 
    header = conn.recv(4)
    if not header:
        return None

   
    message_size = struct.unpack('!I', header)[0]

  
    message = conn.recv(message_size).decode()


    ending_sequence = conn.recv(1).decode()  
    if ending_sequence != "0":
        print("Invalid ending sequence. Message may be corrupted.")

    return message


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 9999))
s.listen(1)


conn, addr = s.accept()

while True:
    try:
   
        received_message = receive_message(conn)
        if received_message is None:
            break

        print(f"Received message from client: {received_message}")

      
        try:
            result = eval(received_message)
            if isinstance(result, int) and -2**31 <= result < 2**31:
                result_bytes = struct.pack('!i', result)
            else:
                result_bytes = b"Error: Result is not within the valid range."

        except Exception as e:
            result_bytes = f"Error: {e}".encode()

   
        conn.send(struct.pack('!I', len(result_bytes)) + result_bytes + "0".encode())

    except socket.error:
        print("Error occurred.")
        break


conn.close()
