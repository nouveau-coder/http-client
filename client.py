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
    
def connect_to_server(ip_addr):
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
    finally:
        socket_obj.close()

def main():
    parser = argparse.ArgumentParser(prog = "client.py")
    parser.add_argument("host_name")
    args = parser.parse_args()
    ip_addr = resolve_hostname(args.host_name)
    if ip_addr:
        connect_to_server(ip_addr)
    
if __name__ == "__main__":
    main()



