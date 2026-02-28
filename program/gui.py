# scanner.py

import socket

# Common port-service mapping
COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

# Attempts to connect to a single port on the target host.
# Returns a tuple of (port, service_name) if the port is open, or None if it's closed/unreachable.
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target, port))
        sock.close()

        if result == 0:
            service = COMMON_SERVICES.get(port, "Unknown Service")
            return (port, service)
        else:
            return None

    except socket.error:
        return None


# Scans a range of ports (inclusive) on the target host.
# Returns a list of (port, service_name) tuples for all open ports found.

def scan_range(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        result = scan_port(target, port)
        if result:
            open_ports.append(result)

    return open_ports
