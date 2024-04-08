import socket

def receive_txt_file(save_path, listen_ip, listen_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((listen_ip, listen_port))
        print("Listening for connections on", listen_ip, ":", listen_port)

        s.listen()

        conn, addr = s.accept()
        print("Connected to", addr)

        file_size = int.from_bytes(conn.recv(4), byteorder='big')

        received_data = bytearray()
        while len(received_data) < file_size:
            chunk = conn.recv(4096)
            if not chunk:
                break
            received_data.extend(chunk)

        with open(save_path, "wb") as file:
            file.write(received_data)

        print("File received and saved to", save_path)

save_path = input("Type save path. ")
listen_ip = "0.0.0.0"
listen_port = int(input("Type port. ")) 

receive_txt_file(save_path, listen_ip, listen_port)
