import socket
import sys
import time


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 3344
    timeout_seconds = 5

    with socket.create_connection((host, port), timeout=timeout_seconds) as sock:
        print(f"Connected to {host}:{port}")
        sock.settimeout(timeout_seconds)
        while True:
            try:
                data = sock.recv(4096)
                if not data:
                    print("Server closed the connection")
                    break
                print(data.decode("utf-8", errors="replace"), end="")
            except socket.timeout:
                continue
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break


if __name__ == "__main__":
    main()
