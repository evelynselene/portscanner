import socket


def scan_port(host, port, timeout=1.0):
    """return True if a TCP connection to host:port succeeds."""
    try:
        with socket.create_connection((host,port), timeout=timeout):
            return True
    except OSError:
        return False


if __name__ == "__main__":
    print(scan_port("127.0.0.1", 445))