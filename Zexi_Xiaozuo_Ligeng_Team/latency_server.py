import socket
import time

def server(host='0.0.0.0', port=12345, marker="PING"):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decoded_data = data.decode()
                if marker in decoded_data:

                    timestamp = float(decoded_data.split('|')[0])
                    recv_time = time.time()
                    delay = recv_time - timestamp
                    print(f"Received time: {timestamp}, Delay: {delay}")

                    conn.sendall(str(delay).encode())

if __name__ == "__main__":
    server()
