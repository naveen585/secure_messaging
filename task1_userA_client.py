import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# using localhost for the connection.
server_host = "127.0.0.1"
server_port = 6789
client_socket.connect((server_host, server_port))
# For Communication
while True:
    client_response = input("Send your response message for User B (type 'exit' to end): ")
    client_socket.sendall(client_response.encode())
    if client_response.lower() == 'exit':
        break
    server_data = client_socket.recv(1024)
    print(f"The message received from User B: {server_data.decode()}")
    if server_data.decode().lower() == 'exit':
        print("Connection closed by User B (Server)")
        break
client_socket.close()
