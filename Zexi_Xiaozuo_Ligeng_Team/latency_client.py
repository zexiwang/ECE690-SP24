import socket
import time

def client(server_ip, port=12345, marker="PING", interval=0.2):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, port))
        try:
            while True:

                timestamp = time.time()
                message = f"{timestamp}|{marker}"
                s.sendall(message.encode())

                data = s.recv(1024)
                delay = float(data.decode())
                current_time = time.time()
                print(f"Time: {current_time}, Estimated one-way delay: {delay * 1000} ms")

                with open("latency_east_no_traffic.txt", "a") as f:
                    f.write(f"Time: {current_time}, Delay: {delay * 1000} ms\n")

                time.sleep(interval)
        except KeyboardInterrupt:
            print("Stopped by user.")

if __name__ == "__main__":
    server_ip = 'ec2-3-85-96-99.compute-1.amazonaws.com'  # Replace with your EC2 instance's IP
    client(server_ip)

