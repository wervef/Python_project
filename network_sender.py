import socket

def network_sender(file_path, target_ip, target_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((target_ip, target_port))
            print("Connected to", target_ip)

            with open(file_path, "rb") as file:
                file_data = file.read()

                s.sendall(len(file_data).to_bytes(4, byteorder='big'))

                s.sendall(file_data)

            print("File sent successfully.")

        except ConnectionRefusedError:
            print("Connection refused. Make sure the target IP and port are correct and the receiver is listening.")
        except FileNotFoundError:
            print("File not found. Make sure the file path is correct.")
        except Exception as e:
            print("An error occurred:", e)


file_path = input("Type file path. ")
target_ip = input("Type target's IP address ")
target_port = int(input("Typer port. "))

network_sender(file_path, target_ip, target_port)
