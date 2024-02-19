import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# using localhost for the connection.
server_host = "127.0.0.1"
server_port = 6789
server_socket.bind((server_host, server_port))
server_socket.listen(3)
# accepting client
client_conn, client_addr = server_socket.accept()
print("Connection has been established.")
# used for two-way messaging.
while True:
    client_data = client_conn.recv(1024)
    if not client_data:
        break
    print(f"The message received from User A is: {client_data.decode()}")
    server_response = input("Send your response for User A (type 'exit' to end): ")
    client_conn.sendall(server_response.encode())
    if server_response.lower() == 'exit':
        print("Connection closed.")
        break
client_conn.close()
