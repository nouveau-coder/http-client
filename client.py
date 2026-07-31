import socket, argparse

def resolve_hostname(hostname):
    try:
        ip_addr = socket.gethostbyname(hostname)
    except socket.gaierror:
        print("hostname cannot be resolved")
        return None
    except OSError as e:
        print(f"Exception: {e}")
        return None
    else:
        return ip_addr

def create_and_send_request(socket_obj,hostname):
    request = (
    "GET / HTTP/1.1\r\n"
    f"Host: {hostname}\r\n"
    "\r\n"
)
    request_bytes = request.encode("utf-8")
    socket_obj.sendall(request_bytes)
    response_bytes = socket_obj.recv(1024)
    response = response_bytes.decode("utf-8")
    print(f"{response}")

def connect_to_server(ip_addr, hostname):
    try:
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_obj.settimeout(1)            
        socket_obj.connect((ip_addr,80))
    except TimeoutError:
        print("Connection took too long to establish")
        return False
    except OSError as e:
        print(f"Exception: {e}")
        return False
    else:
        print("connection successfully established")
        create_and_send_request(socket_obj, hostname)
    finally:
        socket_obj.close()

def main():
    parser = argparse.ArgumentParser(prog = "client.py")
    parser.add_argument("host_name")
    args = parser.parse_args()
    ip_addr = resolve_hostname(args.host_name)
    if ip_addr:
        connect_to_server(ip_addr,args.host_name)
if __name__ == "__main__":
    main()



