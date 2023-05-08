import socket
import struct

def get_online_players(server):
    try:
        host_port = server.split(":")
        if len(host_port) == 2:
            host, port = host_port[0], int(host_port[1])
        else:
            host, port = host_port[0], 25565
        ip = socket.gethostbyname(host)

        # Send handshake + status request
        handshake = b'\x00\x00' + struct.pack('b', len(host)) + host.encode() + struct.pack('>H', port) + b'\x01'
        status_request = b'\x00'
        request_packet = handshake + status_request

        # Open connection and send request
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)
            sock.connect((ip, port))
            sock.send(request_packet)

            # Read response
            data = b''
            while True:
                buffer = sock.recv(4096)
                if not buffer:
                    break
                data += buffer

        # Decode response using different encodings
        for encoding in ['utf-8', 'utf-16', 'utf-32']:
            try:
                response = data.decode(encoding)
                break
            except UnicodeDecodeError:
                pass

        # Extract player list from response
        player_list = []
        for line in response.split("\n"):
            if "players" in line:
                player_list = line[line.index(":")+2:-1].split(", ")
                break
        return player_list

    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press enter to exit...")

server = input("Enter the subdomain or IP address of the server: ")
players = get_online_players(server)
print(f"Online players: {', '.join(players)}")
input("Press enter to exit...")
