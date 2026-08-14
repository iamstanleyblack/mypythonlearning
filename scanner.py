import socket
import fire

def scan(target, ports):
    results = {}

    if isinstance(ports, str):
        port_iter = map(int, ports.split(","))
    elif isinstance(ports, (list, tuple)):
        port_iter = ports
    else:
        raise ValueError("Ports must be a coma-separated string , a list/tuple of ints, or a single int.")
    
    for port in port_iter:
        try: 
            with socket.create_connection((target, port), timeout=1):
                results[port] = "open"
        except(socket.timeout, ConnectionRefusedError, OSError):
            results[port] = "closed"

    for port, status in results.items():
        print(f"Port {port}: {status}")
        return results
    
if __name__ == "__main__":
        fire.Fire(scan)