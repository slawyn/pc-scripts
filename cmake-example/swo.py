import socket
import sys

# STM32 Configuration
CPU_FREQ = 16_000_000  # Set this to your STM32 core clock (e.g., 180MHz)

def process_dwt_data(raw_payload, last_cycle):
    """
    Expects raw_payload to be 4 bytes (uint32_t).
    Calculates elapsed cycles/time since the last transmission.
    """
    # Convert the 4 bytes into a 32-bit integer (little-endian)
    current_cycle = int.from_bytes(raw_payload, byteorder='little')
    
    if last_cycle != 0:
        # Calculate difference, handling the 32-bit counter overflow
        diff_cycles = (current_cycle - last_cycle) & 0xFFFFFFFF
        seconds = diff_cycles / CPU_FREQ
        print(f"Cycle Count: {current_cycle:10} | Δ: {diff_cycles:10} | Time: {seconds:.6f} s")
    
    return current_cycle

def main() -> None:
    host = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 3344
    
    print(f"Connecting to {host}:{port}...")
    
    try:
        with socket.create_connection((host, port), timeout=5) as sock:
            print("Connected. Listening for DWT stream...")
            pending = bytearray()
            last_cycle = 0
            
            while True:
                chunk = sock.recv(4096)
                if not chunk: break
                pending.extend(chunk)

                i = 0
                while i < len(pending):
                    header = pending[i]
                    
                    # 1. Skip Timestamp Packets (0xC0-0xFF)
                    if (header & 0xC0) == 0xC0:
                        i += 1
                        continue

                    # 2. VALIDATE HEADER: Only Port 0 (header 0x03) 
                    # If it's not 0x03, it's garbage/dropped data.
                    if header != 0x03:
                        i += 1 # Skip one byte and try again
                        continue
                    
                    # 3. Process confirmed 4-byte payload
                    if i + 5 <= len(pending):
                        payload = pending[i + 1 : i + 5]
                        last_cycle = process_dwt_data(payload, last_cycle)
                        i += 5 # Move past header + 4 bytes
                    else:
                        break # Incomplete packet, wait for more data
                
                del pending[:i]

    except (socket.error, KeyboardInterrupt):
        print("\nDisconnected.")

if __name__ == "__main__":
    main()