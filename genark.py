import socket
ascii_banner = pyfiglet.figlet_format("GenArk")
print(ascii_banner)

def scan_ports(target, start_port, end_port):
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((target, port))
                open_ports.append(port)
        except (socket.timeout, ConnectionRefusedError):
            pass

    return open_ports

if __name__ == "__main__":
    target_host = input("Enter the target host: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("Open ports on {}:".format(target_host))
        for port in open_ports:
            print("Port {} is open".format(port))
    else:
        print("No open ports found on {}.".format(target_host))
