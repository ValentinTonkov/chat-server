import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ("192.168.1.142", 1080)  # change the ip address
s.bind(server_address)
s.listen(3)


def start_server():
    conn, addr = s.accept()
    try:
        request = conn.recv(1024)
        request = request.decode("utf-8")
        request = request.strip()
        if request != '':
            print("recv: " + request)
            response = input("send: ")
            conn.send(response.encode("utf-8"))
    except Exception as e:
        time.sleep(1)
        print("error", e)
        conn.close()


if __name__ == "__main__":
    while True:
        start_server()
