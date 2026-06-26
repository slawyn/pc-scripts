import socket
import sys


def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 3344

    with socket.create_connection((host, port), timeout=5) as sock:
        print(f"Connected to {host}:{port}")
        while True:
            try:
                data = sock.recv(4096)
                if not data:
                    print("Server closed the connection")
                    break
                print(data.decode("utf-8", errors="replace"), end="")
            except KeyboardInterrupt:
                print("\nInterrupted by user")
                break


if __name__ == "__main__":
    main()
