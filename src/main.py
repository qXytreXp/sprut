# elif sys_args[0] == "recieve":
#     sock.connect(("127.0.0.1", 8000))

#     logging.info("Client connected")

#     accept = input("Accept files?(Y/n): ").lower()

#     match accept:
#         case "y":
#             sock.send("data accepted".encode())
#         case _:
#             sock.close()
#             exit()

#     while True:
#         filename = sock.recv(1024).decode()
#         if not filename:
#             break
#         recieve_files_from_server(server_socket=sock, filename=filename)

#     logging.info("Data succussful transferred")


# sock.close()
import logging
import sys

from tcp.tcp import (
    sock, 
    init_server,
    connect_to_server, 
    recieve_files_from_server,
    send_file_to_client
)


if __name__ == "__main__":
    sys_args = sys.argv[1:]

    match sys_args[0].strip():
        case "send":
            server = init_server(host="127.0.0.1", port=8000)
            client, addrs = server.accept()
            logging.info(f"Connection: {addrs}")

            files = sys_args[1:]  # Select input files name, except command "send"

            if client.recv(1024).decode() == "data accepted":
                logging.info("Sending files...")
                for file_ in files:
                    send_file_to_client(client=client, path_to_file=file_)
                logging.info("Data succussful transferred")

            client.close()

        case "recieve":
            server = connect_to_server(host="127.0.0.1", port=8000)

            accept = input("Accept files?(Y/n): ").lower()

            if accept == "y":
                server.send("data accepted".encode())
            else:
                server.close()
                exit()

            while True:
                filename = server.recv(1024).decode()
                if not filename:
                    break
                recieve_files_from_server(server=server, filename=filename)

            logging.info("Data succussful transferred")
            server.close()
        case _:
            print("Wrong Command")
            sock.close()